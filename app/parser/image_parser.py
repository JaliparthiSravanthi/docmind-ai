
import easyocr
import os

image_path = "data/input/sample_image.png"
output_path = "data/output/ocr_text.txt"

reader = easyocr.Reader(['en'])

results = reader.readtext(image_path)

os.makedirs("data/output", exist_ok=True)

with open(output_path, "w", encoding="utf-8") as file:
    for result in results:
        text = result[1]
        confidence = result[2]

        if confidence > 0.5:
             file.write(f"{text}\n")
        print(f"Text: {text} | Confidence: {confidence:.2f}")

print(f"\nOCR completed successfully.\nSaved to: {output_path}")