import json
import os

# Read products
with open('data/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# Image mapping (same as productImages.ts)
image_map = {
    # AYAM
    "kandang-ayam-baterai-4p-120-eco": "/assets/image/AYAM/1 TINGKAT/4P120 01.png",
    "kandang-ayam-baterai-4p-110-eco": "/assets/image/AYAM/1 TINGKAT/4P110 01.png",
    "kandang-ayam-baterai-6p-110-eco": "/assets/image/AYAM/1 TINGKAT/6P110 01.png",
    "kandang-ayam-baterai-industrial": "/assets/image/AYAM/1 TINGKAT/Baterai Utama.png",
    "paket-fullset-indus-2-tingkat-tipe-a": "/assets/image/AYAM/2 TINGKAT/Fullset Utama 2 Tingkat.png",
    "paket-fullset-indus-2-tingkat-tipe-b": "/assets/image/AYAM/2 TINGKAT/Fullset Utama 2 Tingkat (2).png",
    "paket-fullset-indus-2-tingkat-tipe-c": "/assets/image/AYAM/2 TINGKAT/Fullset Utama 2 Tingkat (3).png",
    "paket-fullset-indus-3-tingkat": "/assets/image/AYAM/3 TINGKAT/Fullset Utama.png",
    "paket-fullset-indus-3-tingkat-box": "/assets/image/AYAM/3 TINGKAT/Fullset Utama (2).png",
    "paket-panggung-4p110-eco": "/assets/image/AYAM/1 TINGKAT/4P110 01.png",
    "paket-panggung-4p110-industrial": "/assets/image/AYAM/1 TINGKAT/4P110 02.png",
    "paket-panggung-4p120-eco": "/assets/image/AYAM/1 TINGKAT/4P120 01.png",
    "paket-panggung-4p120-industrial": "/assets/image/AYAM/1 TINGKAT/4P120 02.png",
    "paket-panggung-6p110-eco": "/assets/image/AYAM/1 TINGKAT/6P110 01.png",
    "paket-panggung-6p110-industrial": "/assets/image/AYAM/1 TINGKAT/6P110 02.png",
    
    # PUYUH
    "kandang-puyuh-l25-talang": "/assets/image/PUYUH/L25/L25 Utama.png",
    "kandang-puyuh-l25-otomatis": "/assets/image/PUYUH/L25/L25TMO.png",
    "kandang-puyuh-l50-talang": "/assets/image/PUYUH/L50-200/L50 Utama.png",
    "kandang-puyuh-l50-otomatis": "/assets/image/PUYUH/L50-200/L50TMO.png",
    "kandang-puyuh-l60-talang": "/assets/image/PUYUH/L60-250/L60 Utama.png",
    "kandang-puyuh-l60-otomatis": "/assets/image/PUYUH/L60-250/L60TMO.png",
    "fullset-puyuh-200-ekor-rangka-hollow": "/assets/image/PUYUH/L50-200/Fullset 200 Utama.png",
    "fullset-puyuh-200-ekor-rangka-siku": "/assets/image/PUYUH/L50-200/Fullset 200 Utama (2).png",
    "fullset-puyuh-250-ekor-rangka-hollow": "/assets/image/PUYUH/L60-250/Fullset 250 utama.png",
    "fullset-puyuh-250-ekor-rangka-siku": "/assets/image/PUYUH/L60-250/Fullset 250 utama (2).png",
    
    # KELINCI
    "kandang-kelinci-carrier-xl": "/assets/image/KELINCI/XL Utama.png",
    "kandang-kelinci-carrier-l": "/assets/image/KELINCI/L Utama.png",
    "kandang-kelinci-carrier-m": "/assets/image/KELINCI/M Utama.png",
}

# Check which products have images
print("Product Image Mapping Status:")
print("=" * 60)

matched = 0
unmatched = []

for p in products:
    pid = p['id']
    if pid in image_map:
        img_path = "public" + image_map[pid]
        exists = os.path.exists(img_path)
        status = "✅" if exists else "❌ FILE NOT FOUND"
        print(f"{status} {p['title'][:50]}")
        if exists:
            matched += 1
    else:
        print(f"⚠️  NO MAPPING: {p['title'][:50]}")
        unmatched.append(pid)

print("\n" + "=" * 60)
print(f"Matched: {matched}/{len(products)}")
print(f"Unmatched: {len(unmatched)}")

if unmatched:
    print("\nProducts without image mapping:")
    for uid in unmatched:
        prod = next(p for p in products if p['id'] == uid)
        print(f"  - {uid} | {prod['title']}")
