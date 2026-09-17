import faiss
import numpy as np
import pickle

# Load embeddings
embeddings = np.load("data/output/embeddings.npy")

# Load stored text
with open("data/output/vector_store.pkl", "rb") as file:
    vector_store = pickle.load(file)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Add embeddings
index.add(embeddings.astype("float32"))

# Save index
faiss.write_index(index, "data/output/faiss_index.index")

print("FAISS index created successfully!")
print(f"Total vectors stored: {index.ntotal}")
print(f"Vector dimension: {dimension}")