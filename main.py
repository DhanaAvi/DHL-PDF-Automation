from pypdf import PdfReader, PdfWriter
from pathlib import Path
from classifier import classify_page

INPUT_FILE = "samples/aaaaa-RFR.pdf"
OUTPUT_DIR = "output"

Path(OUTPUT_DIR).mkdir(exist_ok=True)

reader = PdfReader(INPUT_FILE)

groups = {
    "AWB": [],
    "RFR": [],
    "INV": [],
    "DEGREE": [],
    "OTHER": []
}

for page_num, page in enumerate(reader.pages):

    text = page.extract_text() or ""

    doc_type = classify_page(text)

    print(f"Page {page_num + 1}: {doc_type}")

    groups[doc_type].append(page_num)

for doc_type, pages in groups.items():

    if not pages:
        continue

    writer = PdfWriter()

    for page_num in pages:
        writer.add_page(reader.pages[page_num])

    output_file = f"{OUTPUT_DIR}/{doc_type}.pdf"

    with open(output_file, "wb") as f:
        writer.write(f)

    print(f"Created: {output_file}")