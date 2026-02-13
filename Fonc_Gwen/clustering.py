import numpy as np
import json
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.manifold import TSNE
import plotly.express as px
import matplotlib.pyplot as plt

# =========================
# CONFIG
# =========================
FEATURES_FILE = "pokemon_features.npy"
LABELS_FILE = "pokemon_labels.npy"
CLASSMAP_FILE = "class_to_idx.json"

# Cluster analysis settings
K_RANGE = range(10, 101, 10)  # test clusters from 10 to 100
DEFAULT_NUM_CLUSTERS = 50      # final clusters for t-SNE plot

# t-SNE settings
TSNE_PERPLEXITY = 30
TSNE_LR = 200
TSNE_MAX_ITER = 1000

# Plotly HTML output
HTML_FILE = "pokemon_clusters_tsne.html"

# =========================
# LOAD DATA
# =========================
features = np.load(FEATURES_FILE)
labels = np.load(LABELS_FILE)

with open(CLASSMAP_FILE, "r") as f:
    class_to_idx = json.load(f)
idx_to_class = {v: k for k, v in class_to_idx.items()}

names = [idx_to_class[int(l)] for l in labels]

# =========================
# AUTOMATIC SUGGESTION OF K
# =========================
print("Running cluster analysis for K selection...")
inertia_list = []
silhouette_list = []

for k in K_RANGE:
    kmeans = KMeans(n_clusters=k, random_state=42)
    cluster_ids = kmeans.fit_predict(features)
    inertia_list.append(kmeans.inertia_)
    score = silhouette_score(features, cluster_ids)
    silhouette_list.append(score)
    print(f"K={k} -> Inertia={kmeans.inertia_:.2f}, Silhouette={score:.4f}")

# Plot elbow + silhouette
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(K_RANGE, inertia_list, marker='o')
plt.xlabel("Number of clusters K")
plt.ylabel("Inertia")
plt.title("Elbow Method")

plt.subplot(1, 2, 2)
plt.plot(K_RANGE, silhouette_list, marker='o')
plt.xlabel("Number of clusters K")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Analysis")
plt.tight_layout()
plt.show()

# =========================
# FINAL K-MEANS CLUSTERING
# =========================
print(f"Running final K-Means with K={DEFAULT_NUM_CLUSTERS}...")
kmeans = KMeans(n_clusters=DEFAULT_NUM_CLUSTERS, random_state=42)
cluster_ids = kmeans.fit_predict(features)
print("Clustering done!")

# =========================
# t-SNE REDUCTION
# =========================
print("Running t-SNE for 2D visualization...")
tsne = TSNE(
    n_components=2,
    perplexity=TSNE_PERPLEXITY,
    learning_rate=TSNE_LR,
    max_iter=TSNE_MAX_ITER,
    random_state=42
)
features_2d = tsne.fit_transform(features)
print("t-SNE done!")

# =========================
# PLOT WITH PLOTLY
# =========================
df = pd.DataFrame({
    "x": features_2d[:, 0],
    "y": features_2d[:, 1],
    "cluster": cluster_ids.astype(str),  # categorical colors
    "name": names
})

fig = px.scatter(
    df,
    x="x",
    y="y",
    color="cluster",
    hover_name="name",
    title=f"Pokémon embeddings clustered (K={DEFAULT_NUM_CLUSTERS}, t-SNE + hover labels)",
    width=1200,
    height=800
)

fig.update_traces(marker=dict(size=8, opacity=0.7))

# Save and open interactive HTML
fig.write_html(HTML_FILE, auto_open=False)
print(f"Saved interactive plot to {HTML_FILE}")
