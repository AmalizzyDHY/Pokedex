import cv2
import torch
import torch.nn as nn
import numpy as np
from cnn_train import PokemonCNN, IMAGE_SIZE  # reuse the model definition

# -----------------------------
# CONFIG
# -----------------------------
MODEL_PATH = "pokemon_cnn.pt"   # your trained model
QUERY_IMAGE = "test.png"        # image to identify

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# -----------------------------
# LOAD MODEL
# -----------------------------
checkpoint = torch.load(MODEL_PATH, map_location=DEVICE)
classes = checkpoint["classes"]

model = PokemonCNN(len(classes)).to(DEVICE)
model.load_state_dict(checkpoint["model"])
model.eval()

# -----------------------------
# LOAD IMAGE
# -----------------------------
img = cv2.imread(QUERY_IMAGE, cv2.IMREAD_GRAYSCALE)
if img is None:
    raise ValueError(f"Could not load image: {QUERY_IMAGE}")

img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE), interpolation=cv2.INTER_NEAREST)
img = img.astype(np.float32) / 255.0
img_tensor = torch.from_numpy(img).unsqueeze(0).unsqueeze(0).to(DEVICE)  # (1,1,H,W)

# -----------------------------
# PREDICT
# -----------------------------
with torch.no_grad():
    logits = model(img_tensor)
    probs = torch.softmax(logits, dim=1).cpu().numpy()[0]

# -----------------------------
# SHOW TOP-5
# -----------------------------
top5_idx = probs.argsort()[::-1][:5]
print("Top predictions:")
for i in top5_idx:
    print(f"{classes[i]:15s}  prob={probs[i]:.4f}")
