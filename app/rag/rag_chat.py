import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("data/output/faiss_index.index")

# Load vector store
with open("data/output/vector_store.pkl", "rb") as file:
    vector_store = pickle.load(file)

# Ask user a question
query = input("Ask a question: ")

# Convert question into embedding
query_embedding = model.encode([query]).astype("float32")
faiss.normalize_L2(query_embedding)

# Retrieve top 3 chunks
distances, indices = index.search(query_embedding, 3)

# Combine retrieved chunks
context = ""

for i in indices[0]:
    context += vector_store[i]["text"] + "\n\n"

print("\nRetrieved Context:\n")
print(context)