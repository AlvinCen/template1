import json
import os
import re

# Read existing products
with open('data/products.json', 'r', encoding='utf-8') as f:
    existing_products = json.load(f)

existing_ids = set(p['id'] for p in existing_products)
print(f"Current products: {len(existing_products)}")

# Helper functions
def create_product_id(name, category):
    pid = name.lower()
    pid = re.sub(r'[^a-z0-9\s-]', '', pid)
    pid = re.sub(r'\s+', '-', pid)
    pid = re.sub(r'-+', '-', pid)
    return f"{category.lower()}-{pid}".strip('-')

def clean_product_name(filename, category):
    name = os.path.splitext(filename)[0]
    # Remove common suffixes
    name = re.sub(r'\s*\(\d+\)$', '', name)
    name = re.sub(r'\s+(Utama|utama|SPEK|Spek).*$', '', name)
    name = re.sub(r'\s+\d{2,}$', '', name)
    return name.strip()

def create_placeholder_product(filename, category, folder_path):
    product_name = clean_product_name(filename, category)
    product_id = create_product_id(product_name, category.replace(' & ', '-'))
    
    # Skip if already exists
    if product_id in existing_ids:
        return None
    
    # Determine productLine based on folder
    if category == "Kandang Ayam":
        if '1 TINGKAT' in folder_path or '1T' in product_name:
            productLine = "Baterai 1 Tingkat"
        elif '2 TINGKAT' in folder_path or '2T' in product_name:
            productLine = "Fullset 2 Tingkat"
        elif '3 TINGKAT' in folder_path or '3T' in product_name:
            productLine = "Fullset 3 Tingkat"
        else:
            productLine = "Kandang Ayam"
    elif category == "Kandang Kelinci":
        if 'LIPAT' in product_name or 'LIPAT' in folder_path:
            productLine = "Carrier LIPAT"
        elif 'Breeding' in product_name:
            productLine = "Breeding"
        else:
            productLine = "Carrier"
    elif category == "Kandang Burung & Exotic":
        if 'Aviary' in product_name:
            productLine = "Mini Aviary"
        elif 'Umbar' in product_name or 'XXL' in product_name:
            productLine = "Umbaran"
        else:
            productLine = "Kandang Burung"
    else:
        productLine = category
    
    return {
        "id": product_id,
        "category": category,
        "productLine": productLine,
        "title": product_name,
        "subtitle": "Produk sedang habis - Coming Soon",
        "specs": {
            "material": ["Informasi akan segera diupdate"],
            "notes": ["Produk tersedia, mohon hubungi untuk info stok"]
        },
        "features": [
            "Produk berkualitas",
            "Hubungi untuk info stok dan harga"
        ],
        "variants": [{
            "variantName": "Standard",
            "packageContents": ["1 Unit"],
            "price": {
                "min": 0,
                "max": 0,
                "currency": "IDR",
                "rawText": "Hubungi Kami"
            }
        }],
        "images": [{
            "sourcePdf": "Product Photo",
            "page": 1,
            "localPath": folder_path.replace('public', '') + '/' + filename
        }],
        "source": {
            "pdf": "Product Photo Library",
            "pages": [1],
            "rawSnippets": [product_name]
        },
        "needsReview": True,
        "outOfStock": True
    }

# Scan all categories
categories_to_scan = {
    'AYAM': 'Kandang Ayam',
    'KELINCI': 'Kandang Kelinci',
    'BURUNG': 'Kandang Burung & Exotic'
}

new_products = []
skipped_spec_files = 0

for folder, category in categories_to_scan.items():
    base_path = f'public/assets/image/{folder}'
    
    if not os.path.exists(base_path):
        print(f"⚠️ Folder {base_path} not found")
        continue
    
    # Walk through all subdirectories
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if not file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                continue
            
            # Skip spec/technical images
            if any(x in file.lower() for x in ['spek', 'spesifikasi', 'eco vs industrial']):
                skipped_spec_files += 1
                continue
            
            folder_path = os.path.join(root, file)
            product = create_placeholder_product(file, category, folder_path)
            
            if product:
                new_products.append(product)
                existing_ids.add(product['id'])  # Add to set to avoid duplicates

print(f"\n📊 SCAN RESULTS:")
print(f"New products created: {len(new_products)}")
print(f"Skipped (spec files): {skipped_spec_files}")
print(f"Skipped (duplicates): Many")

print(f"\n📦 BY CATEGORY:")
ayam_count = len([p for p in new_products if p['category'] == 'Kandang Ayam'])
kelinci_count = len([p for p in new_products if p['category'] == 'Kandang Kelinci'])
burung_count = len([p for p in new_products if p['category'] == 'Kandang Burung & Exotic'])

print(f"Kandang Ayam: {ayam_count}")
print(f"Kandang Kelinci: {kelinci_count}")
print(f"Kandang Burung: {burung_count}")

print(f"\n📝 SAMPLE NEW PRODUCTS:")
for p in new_products[:15]:
    print(f"  - {p['category']:25} | {p['title'][:50]}")

# Merge and save
all_products = existing_products + new_products
print(f"\n✅ TOTAL: {len(existing_products)} + {len(new_products)} = {len(all_products)} products")

with open('data/products.json', 'w', encoding='utf-8') as f:
    json.dump(all_products, f, ensure_ascii=False, indent=4)

print("\n✅ Updated products.json successfully!")

# Save new products for image mapping generation
with open('new_products_for_mapping.json', 'w', encoding='utf-8') as f:
    json.dump(new_products, f, ensure_ascii=False, indent=2)
