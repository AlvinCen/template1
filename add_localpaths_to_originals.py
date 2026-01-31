import json

# Read products and existing image mappings
with open('data/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# Manual mapping for original 31 products that don't have localPath
original_mappings = {
    # AYAM ECO
    "kandang-ayam-baterai-4p-120-eco": "/assets/image/AYAM/1 TINGKAT/4P120 01.png",
    "kandang-ayam-baterai-4p-110-eco": "/assets/image/AYAM/1 TINGKAT/4P110 01.png",
    "kandang-ayam-baterai-6p-110-eco": "/assets/image/AYAM/1 TINGKAT/6P110 01.png",
    
    # AYAM Industrial
    "kandang-ayam-baterai-industrial": "/assets/image/AYAM/1 TINGKAT/Baterai Utama.png",
    
    # PUYUH
    "kandang-puyuh-l25-talang": "/assets/image/PUYUH/L25/L25 Utama.png",
    "kandang-puyuh-l25-otomatis": "/assets/image/PUYUH/L25/L25TMO.png",
    "kandang-puyuh-l50-talang": "/assets/image/PUYUH/L50-200/L50 Utama.png",
    "kandang-puyuh-l50-otomatis": "/assets/image/PUYUH/L50-200/L50TMO.png",
    "kandang-puyuh-l60-talang": "/assets/image/PUYUH/L60-250/L60 Utama.png",
    "kandang-puyuh-l60-otomatis": "/assets/image/PUYUH/L60-250/L60TMO.png",
    
    # PUYUH Fullset
    "fullset-puyuh-200-ekor-rangka-hollow": "/assets/image/PUYUH/L50-200/Fullset 200 Utama.png",
    "fullset-puyuh-200-ekor-rangka-siku": "/assets/image/PUYUH/L50-200/Fullset 200 Utama (2).png",
    "fullset-puyuh-250-ekor-rangka-hollow": "/assets/image/PUYUH/L60-250/Fullset 250 utama.png",
    "fullset-puyuh-250-ekor-rangka-siku": "/assets/image/PUYUH/L60-250/Fullset 250 utama (2).png",
    
    # KELINCI
    "kandang-kelinci-carrier-xl": "/assets/image/KELINCI/XL Utama.png",
    "kandang-kelinci-carrier-l": "/assets/image/KELINCI/L Utama.png",
    "kandang-kelinci-carrier-m": "/assets/image/KELINCI/M Utama.png",
    "kandang-kelinci-breeding-2-hole": "/assets/image/KELINCI/Kandang Kelinci Breeding 1.png",
    
    # BURUNG
    "mini-aviary-120x70x150": "/assets/image/BURUNG/Aviary 120x70.png",
    "mini-aviary-120x50x150": "/assets/image/BURUNG/Aviary 120x50.png",
    "mini-aviary-90x60x150": "/assets/image/BURUNG/Aviary 90x60.png",
    "umbaran-burung-m": "/assets/image/BURUNG/M Utama BRG.png",
    "umbaran-burung-l": "/assets/image/BURUNG/L Utama BRG.png",
    "umbaran-burung-xl": "/assets/image/BURUNG/XL Utama BRG.png",
    
    # PANGGUNG
    "paket-panggung-4p110-eco": "/assets/image/AYAM/1 TINGKAT/4P110 01.png",
    "paket-panggung-4p110-industrial": "/assets/image/AYAM/1 TINGKAT/4P110 02.png",
    "paket-panggung-4p120-eco": "/assets/image/AYAM/1 TINGKAT/4P120 01.png",
    "paket-panggung-4p120-industrial": "/assets/image/AYAM/1 TINGKAT/4P120 02.png",
    "paket-panggung-6p110-eco": "/assets/image/AYAM/1 TINGKAT/6P110 01.png",
    "paket-panggung-6p110-industrial": "/assets/image/AYAM/1 TINGKAT/6P110 02.png",
    
    # FULLSET Industrial
    "paket-fullset-indus-2-tingkat-tipe-a": "/assets/image/AYAM/2 TINGKAT/Fullset Utama 2 Tingkat.png",
    "paket-fullset-indus-2-tingkat-tipe-b": "/assets/image/AYAM/2 TINGKAT/Fullset Utama 2 Tingkat (2).png",
    "paket-fullset-indus-2-tingkat-tipe-c": "/assets/image/AYAM/2 TINGKAT/Fullset Utama 2 Tingkat (3).png",
    "paket-fullset-indus-3-tingkat": "/assets/image/AYAM/3 TINGKAT/Fullset Utama 4P (2).png",
    "paket-fullset-indus-3-tingkat-box": "/assets/image/AYAM/3 TINGKAT/Fullset Utama (2).png",
}

# Add localPath to products that don't have it
added_count = 0

for p in products:
    if 'images' in p and len(p['images']) > 0:
        # Check if first image doesn't have localPath
        if 'localPath' not in p['images'][0]:
            # Try to find mapping
            if p['id'] in original_mappings:
                p['images'][0]['localPath'] = original_mappings[p['id']]
                added_count += 1
                print(f"Added localPath to: {p['id']}")

print(f"\n✅ Added localPath to {added_count} products")

# Save
with open('data/products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=4)

print("✅ Saved products.json")

# Verify all products now have localPath
missing = []
for p in products:
    if 'images' in p and len(p['images']) > 0:
        if 'localPath' not in p['images'][0]:
            missing.append(p['id'])

print(f"\nProducts still without localPath: {len(missing)}")
if missing:
    print("Missing:")
    for m in missing[:10]:
        print(f"  - {m}")
