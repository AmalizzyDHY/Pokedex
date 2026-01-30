import cv2
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from pathlib import Path
from tqdm import tqdm
import random
import numpy as np

# -----------------------------
# CONFIG
# -----------------------------
SPRITE_DIR = "poke_pics"
IMAGE_SIZE = 64
BATCH_SIZE = 64
EPOCHS = 20
LR = 1e-3
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# -----------------------------
# DATASET
# -----------------------------
class PokemonDataset(Dataset):
    def __init__(self, sprite_dir, augment=False):
        self.paths = sorted(Path(sprite_dir).glob("*.png"))
        self.augment = augment

        names = [p.stem.split("_")[0] for p in self.paths]
        self.classes = sorted(set(names))
        self.class_to_idx = {c: i for i, c in enumerate(self.classes)}

    def __len__(self):
        return len(self.paths)

    def _augment(self, img):
        # Horizontal flip
        if random.random() < 0.5:
            img = cv2.flip(img, 1)

        # Small translation (pixel-art safe)
        tx = random.randint(-2, 2)
        ty = random.randint(-2, 2)
        M = np.float32([[1, 0, tx], [0, 1, ty]])
        img = cv2.warpAffine(
            img, M, (IMAGE_SIZE, IMAGE_SIZE),
            flags=cv2.INTER_NEAREST,
            borderValue=0
        )

        return img

    def __getitem__(self, idx):
        path = self.paths[idx]
        label_name = path.stem.split("_")[0]
        label = self.class_to_idx[label_name]

        img = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE),
                         interpolation=cv2.INTER_NEAREST)

        if self.augment:
            img = self._augment(img)

        img = img.astype(np.float32) / 255.0
        img = torch.from_numpy(img).unsqueeze(0)  # (1, H, W)

        return img, label

# -----------------------------
# MODEL
# -----------------------------
class PokemonCNN(nn.Module):
    def __init__(self, num_classes):
        super().__init__()

        self.features = nn.Sequential(
            nn.Conv2d(1, 32, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 64, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * 16 * 16, 512),
            nn.ReLU(),
            nn.Linear(512, num_classes)
        )

    def forward(self, x):
        x = self.features(x)
        return self.classifier(x)

# -----------------------------
# TRAINING
# -----------------------------
def train():
    dataset = PokemonDataset(SPRITE_DIR, augment=True)
    loader = DataLoader(dataset, batch_size=BATCH_SIZE,
                        shuffle=True, num_workers=2)

    model = PokemonCNN(len(dataset.classes)).to(DEVICE)
    optimizer = optim.Adam(model.parameters(), lr=LR)
    criterion = nn.CrossEntropyLoss()

    for epoch in range(EPOCHS):
        model.train()
        total_loss = 0
        correct = 0
        total = 0

        for imgs, labels in tqdm(loader, desc=f"Epoch {epoch+1}/{EPOCHS}"):
            imgs, labels = imgs.to(DEVICE), labels.to(DEVICE)

            optimizer.zero_grad()
            logits = model(imgs)
            loss = criterion(logits, labels)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            preds = logits.argmax(dim=1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)

        acc = correct / total * 100
        print(f"Epoch {epoch+1}: loss={total_loss:.3f} acc={acc:.2f}%")

    torch.save({
        "model": model.state_dict(),
        "classes": dataset.classes
    }, "pokemon_cnn.pt")

    print("Saved model to pokemon_cnn.pt")

# -----------------------------
# ENTRY
# -----------------------------
if __name__ == "__main__":
    train()
