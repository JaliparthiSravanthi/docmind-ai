
from sentence_transformers import SentenceTransformer
import numpy as np
import os

input_path = "data/output/chunks.txt"
output_path = "data/output/embeddings.npy"
metadata_path = "data/output/chunks_metadata.txt"

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

with open(input_path, "r", encoding="utf-8") as file:
    text = file.read()

chunks = []

for part in text.split("===== Chunk"):
    part = part.strip()
    if part:
        lines = part.split("\n", 1)
        if len(lines) > 1:
            chunks.append(lines[1].strip())

print(f"Total Chunks Loaded: {len(chunks)}")

embeddings = model.encode(chunks)

os.makedirs("data/output", exist_ok=True)

np.save(output_path, embeddings)

with open(metadata_path, "w", encoding="utf-8") as file:
    for i, chunk in enumerate(chunks):
        file.write(f"Chunk {i+1}\n")
        file.write(chunk)
        file.write("\n\n")

print(f"Embedding Shape: {embeddings.shape}")
print(f"Embeddings saved to: {output_path}")
print(f"Metadata saved to: {metadata_path}")