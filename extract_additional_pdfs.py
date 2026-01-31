import PyPDF2
import json
import os

pdf_files = [
    "KANDANG PANGGUNG.pdf",
    "NET ALL PRODUCT.pdf"
]

all_data = {}

for pdf_file in pdf_files:
    if not os.path.exists(pdf_file):
        print(f"File not found: {pdf_file}")
        continue
    
    print(f"\n{'='*80}")
    print(f"EXTRACTING: {pdf_file}")
    print(f"{'='*80}\n")
    
    pages_text = []
    
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        
        print(f"Total pages: {num_pages}\n")
        
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            pages_text.append({
                "page": page_num + 1,
                "text": text
            })
            
            print(f"--- PAGE {page_num + 1} ---")
            print(text[:800] if len(text) > 800 else text)
            print("\n")
    
    all_data[pdf_file] = {
        "total_pages": num_pages,
        "pages": pages_text
    }

# Save to JSON file for further analysis
with open('extracted_additional_pdfs.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print(f"\n{'='*80}")
print("Extraction complete! Data saved to extracted_additional_pdfs.json")
print(f"{'='*80}")
