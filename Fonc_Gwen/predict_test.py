import json
import torch
import torch.nn as nn
from PIL import Image
import torchvision.transforms as T
import torchvision.models as models

# =========================
# CONFIG
# =========================
MODEL_PATH = "pokemon_cnn.pt"
CLASSMAP_PATH = "class_to_idx.json"
IMG_PATH = "test.png"
IMG_SIZE = 128
TOP_K = 5
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# =========================
# LOAD CLASS MAP
# =========================
with open(CLASSMAP_PATH, "r") as f:
    class_to_idx = json.load(f)

idx_to_class = {v: k for k, v in class_to_idx.items()}
num_classes = len(idx_to_class)

# =========================
# MODEL
# =========================
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
for param in model.parameters():
    param.requires_grad = False

model.fc = nn.Linear(model.fc.in_features, num_classes)
model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
model = model.to(DEVICE)
model.eval()

# =========================
# IMAGE TRANSFORM
# =========================
transform = T.Compose([
    T.Resize((IMG_SIZE, IMG_SIZE)),
    T.ToTensor(),
])

# handle alpha channel / transparent PNG
def load_image(path):
    img = Image.open(path).convert("RGBA")
    bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
    img = Image.alpha_composite(bg, img).convert("RGB")
    return img

img = load_image(IMG_PATH)
img_t = transform(img).unsqueeze(0).to(DEVICE)  # add batch dimension

# =========================
# PREDICTION
# =========================
with torch.no_grad():
    out = model(img_t)
    prob = torch.softmax(out, dim=1)
    
    top_probs, top_idxs = torch.topk(prob, k=TOP_K, dim=1)
    
    top_probs = top_probs.cpu().numpy().flatten()
    top_idxs = top_idxs.cpu().numpy().flatten()
    
    print("Top predictions:")
    for i in range(TOP_K):
        cls = idx_to_class[int(top_idxs[i])]
        conf = top_probs[i]
        print(f"{i+1}. {cls} - {conf:.4f}")
