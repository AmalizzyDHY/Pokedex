import cv2
import numpy as np
from pathlib import Path
from tqdm import tqdm

# -----------------------------
# CONFIG
# -----------------------------
SPRITE_DIR = "poke_pics"
IMAGE_SIZE = (64, 64)
TOP_K = 20

# -----------------------------
# IMAGE LOADING (PIXEL ART SAFE)
# -----------------------------
def load_sprite(path, size=IMAGE_SIZE):
    img = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Could not load image: {path}")

    img = cv2.resize(img, size, interpolation=cv2.INTER_NEAREST)
    img = img.astype(np.float32) / 255.0
    return img

# -----------------------------
# BUILD TEMPLATE DATABASE
# -----------------------------
def build_template_db(sprite_dir):
    vectors = []
    labels = []
    paths = []

    sprite_dir = Path(sprite_dir)

    print("Loading sprites...")
    for img_path in tqdm(sorted(sprite_dir.glob("*.png"))):
        filename = img_path.stem  # e.g. Diglett_1_0
        pokemon_name = filename.split("_")[0]

        img = load_sprite(img_path)
        vec = img.flatten()
        vec /= np.linalg.norm(vec) + 1e-8

        vectors.append(vec)
        labels.append(pokemon_name)
        paths.append(img_path.name)

    vectors = np.stack(vectors)
    labels = np.array(labels)

    print(f"Loaded {len(labels)} sprites.")
    return vectors, labels, paths

# -----------------------------
# IDENTIFICATION
# -----------------------------
def identify_pokemon(query_path, template_vectors, template_labels, template_paths, top_k=TOP_K):
    query_img = load_sprite(query_path)
    q = query_img.flatten()
    q /= np.linalg.norm(q) + 1e-8

    similarities = template_vectors @ q

    top_indices = np.argsort(similarities)[::-1][:top_k]

    results = []
    for idx in top_indices:
        results.append({
            "pokemon": template_labels[idx],
            "similarity": float(similarities[idx]),
            "template": template_paths[idx]
        })

    return results

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    template_vectors, template_labels, template_paths = build_template_db(SPRITE_DIR)

    # Example query image
    query_image = "test.png"

    results = identify_pokemon(
        query_image,
        template_vectors,
        template_labels,
        template_paths,
        top_k=TOP_K
    )

    print("\nTop predictions:")
    for r in results:
        print(
            f"{r['pokemon']:15s}  "
            f"sim={r['similarity']:.4f}  "
            f"matched={r['template']}"
        )
