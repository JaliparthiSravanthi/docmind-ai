import pickle
import numpy as np

embeddings = np.load("data/output/embeddings.npy")

with open("data/output/chunks_metadata.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunks = []

for part in text.split("Chunk"):
    part = part.strip()
    if part:
        lines = part.split("\n", 1)
        if len(lines) > 1:
            chunks.append(lines[1].strip())

vector_store = []

for chunk, embedding in zip(chunks, embeddings):
    vector_store.append({
        "text": chunk,
        "embedding": embedding
    })

with open("data/output/vector_store.pkl", "wb") as file:
    pickle.dump(vector_store, file)

print(f"Stored {len(vector_store)} vectors successfully.")
print("Saved to: data/output/vector_store.pkl")