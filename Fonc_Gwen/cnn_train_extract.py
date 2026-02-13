import os
import json
import numpy as np
from PIL import Image
from tqdm import tqdm

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as T
import torchvision.models as models

# =========================
# CONFIG
# =========================
DATA_DIR = "poke_pics"
IMG_SIZE = 128
BATCH_SIZE = 32
EPOCHS = 20
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

MODEL_OUT = "pokemon_cnn.pt"
FEATURES_OUT = "pokemon_features.npy"
LABELS_OUT = "pokemon_labels.npy"
CLASSMAP_OUT = "class_to_idx.json"

# =========================
# DATASET
# =========================
class PokemonDataset(Dataset):
    def __init__(self, root, transform=None):
        self.samples = []
        self.transform = transform

        for fname in os.listdir(root):
            if not fname.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                continue

            # Pokémon name = part before first "_"
            label = fname.split("_")[0]
            path = os.path.join(root, fname)
            self.samples.append((path, label))

        self.classes = sorted(list(set(lbl for _, lbl in self.samples)))
        self.class_to_idx = {c: i for i, c in enumerate(self.classes)}

        self.samples = [
            (p, self.class_to_idx[lbl])
            for p, lbl in self.samples
        ]

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        path, label = self.samples[idx]

        img = Image.open(path).convert("RGB")

        if self.transform:
            img = self.transform(img)

        return img, label

# =========================
# TRANSFORMS
# =========================
train_tf = T.Compose([
    T.Resize((IMG_SIZE, IMG_SIZE)),
    T.RandomHorizontalFlip(),
    T.RandomRotation(15),
    T.ColorJitter(0.2, 0.2, 0.2),
    T.ToTensor(),
])

eval_tf = T.Compose([
    T.Resize((IMG_SIZE, IMG_SIZE)),
    T.ToTensor(),
])

# =========================
# LOAD DATA
# =========================
dataset = PokemonDataset(DATA_DIR, transform=train_tf)

with open(CLASSMAP_OUT, "w") as f:
    json.dump(dataset.class_to_idx, f, indent=2)

loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

num_classes = len(dataset.classes)
print("Classes:", num_classes)
print("Images:", len(dataset))

# =========================
# MODEL (TRANSFER LEARNING)
# =========================
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)

# freeze backbone (important with tiny dataset)
for param in model.parameters():
    param.requires_grad = False

# replace classifier
model.fc = nn.Linear(model.fc.in_features, num_classes)

model = model.to(DEVICE)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.fc.parameters(), lr=1e-3)

# =========================
# TRAINING
# =========================
model.train()

for epoch in range(EPOCHS):
    total_loss = 0

    for imgs, labels in tqdm(loader, desc=f"Epoch {epoch+1}/{EPOCHS}"):
        imgs, labels = imgs.to(DEVICE), labels.to(DEVICE)

        optimizer.zero_grad()
        out = model(imgs)
        loss = criterion(out, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print("Loss:", total_loss / len(loader))

# save model
torch.save(model.state_dict(), MODEL_OUT)
print("Saved model:", MODEL_OUT)

# =========================
# FEATURE EXTRACTION
# =========================
# remove classifier head
feature_extractor = nn.Sequential(*list(model.children())[:-1])
feature_extractor.eval()

# reload dataset without augmentation
dataset_eval = PokemonDataset(DATA_DIR, transform=eval_tf)
loader_eval = DataLoader(dataset_eval, batch_size=BATCH_SIZE)

all_features = []
all_labels = []

with torch.no_grad():
    for imgs, labels in tqdm(loader_eval, desc="Extracting features"):
        imgs = imgs.to(DEVICE)

        feats = feature_extractor(imgs)
        feats = feats.view(feats.size(0), -1)

        all_features.append(feats.cpu().numpy())
        all_labels.append(labels.numpy())

features = np.concatenate(all_features)
labels = np.concatenate(all_labels)

np.save(FEATURES_OUT, features)
np.save(LABELS_OUT, labels)

print("Saved features:", FEATURES_OUT)
