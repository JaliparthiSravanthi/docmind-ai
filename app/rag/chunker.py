
import os

input_path = "data/output/docx_text.txt"
output_path = "data/output/chunks.txt"

CHUNK_SIZE = 300
OVERLAP = 50


def create_chunks(text, chunk_size=300, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        start += chunk_size - overlap
       
    return chunks


with open(input_path, "r", encoding="utf-8") as file:
    text = file.read()

chunks = create_chunks(text, CHUNK_SIZE, OVERLAP)

os.makedirs("data/output", exist_ok=True)

with open(output_path, "w", encoding="utf-8") as file:
    for i, chunk in enumerate(chunks):
        file.write(f"===== Chunk {i+1} =====\n")
        file.write(chunk)
        file.write("\n\n")
        print(f"Chunk {i+1}: {len(chunk)} characters")
print(f"Total Chunks Created: {len(chunks)}")
print(f"Chunks saved to: {output_path}")