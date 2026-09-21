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
faiss.normalize_L2(query_embedding)

# Search top 3 matches
distances, indices = index.search(query_embedding, 3)

print("\nTop Results:\n")

# Get more candidates from FAISS
distances, indices = index.search(query_embedding, 10)

query_words = set(query.lower().split())
results = []

for idx, dist in zip(indices[0], distances[0]):
    text = vector_store[idx]["text"]
    score = float(dist)

    # Give bonus for every matching word
    text_words = set(text.lower().split())
    score += 0.1 * len(query_words & text_words)

    results.append((score, idx))

# Sort by new score
results.sort(reverse=True)

# Show best 3
for rank, (_, idx) in enumerate(results[:3], start=1):
    print(f"Result {rank} (Chunk {idx+1})")
    print(vector_store[idx]["text"][:200])
    print("-" * 50)