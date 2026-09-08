
import pymupdf
import os

# Input and Output paths
pdf_path = "data/input/sample.pdf"
output_path = "data/output/extracted_text.txt"


def extract_text_from_pdf(pdf_file):
    document = pymupdf.open(pdf_file)
    full_text = ""

    print(f"Total Pages: {document.page_count}")

    for page_number in range(document.page_count):
        page = document.load_page(page_number)
        text = page.get_text()

        full_text += f"\n----- Page {page_number + 1} -----\n"
        full_text += text

        print(f"Page {page_number + 1} extracted")

    document.close()
    return full_text


# Create output folder if it doesn't exist
os.makedirs("data/output", exist_ok=True)

# Extract text
text = extract_text_from_pdf(pdf_path)

# Save text to a file
with open(output_path, "w", encoding="utf-8") as file:
    file.write(text)

print(f"\nText saved successfully to: {output_path}")