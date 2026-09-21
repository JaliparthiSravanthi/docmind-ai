import pickle
import numpy as np

# Load embeddings
embeddings = np.load("data/output/embeddings.npy")

# Load the original chunks created by chunker.py
with open("data/output/chunks.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunks = []

# Split using the exact separator written by chunker.py
for part in text.split("===== Chunk"):
    part = part.strip()
    if part:
        lines = part.split("\n", 1)
        if len(lines) > 1:
            chunks.append(lines[1].strip())

# Pair each chunk with its embedding
vector_store = []

for chunk, embedding in zip(chunks, embeddings):
    vector_store.append({
        "text": chunk,
        "embedding": embedding
    })

# Save the vector store
with open("data/output/vector_store.pkl", "wb") as file:
    pickle.dump(vector_store, file)

print(f"Stored {len(vector_store)} vectors successfully.")
print("Saved to: data/output/vector_store.pkl")