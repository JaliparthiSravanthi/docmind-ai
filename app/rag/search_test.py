import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("data/output/faiss_index.index")

# Load vector store
with open("data/output/vector_store.pkl", "rb") as file:
    vector_store = pickle.load(file)

# User question
query = input("Ask a question: ")

# Convert question into embedding
query_embedding = model.encode([query]).astype("float32")

# Search top 3 matches
distances, indices = index.search(query_embedding, 3)

print("\nTop Results:\n")

for i in indices[0]:
    print(vector_store[i]["text"][:200])
    print("-" * 50)