import pickle

with open("data/output/vector_store.pkl", "rb") as file:
    store = pickle.load(file)

print("Total Stored:", len(store))
print(store[0]["text"][:100])
print(len(store[0]["embedding"]))