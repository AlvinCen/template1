import json
import os
import re

# Read existing products
with open('data/products.json', 'r', encoding='utf-8') as f:
    existing_products = json.load(f)

print(f"Current products: {len(existing_products)}")

# Helper function to create product ID
def create_product_id(name, category):
    # Convert to lowercase, replace spaces with hyphens
    pid = name.lower()
    pid = re.sub(r'[^a-z0-9\s-]', '', pid)  # Remove special chars
    pid = re.sub(r'\s+', '-', pid)  # Replace spaces with hyphens
    pid = re.sub(r'-+', '-', pid)  # Remove duplicate hyphens
    return f"{category.lower()}-{pid}".strip('-')

# Helper to extract better names from files
def get_product_info(filename):
    name = os.path.splitext(filename)[0]
    
    # Mapping for better names
    name_mapping = {
        'Ayam Sekat': 'Sekat Kandang Ayam',
        'Bebek Sekat': 'Sekat Kandang Bebek',
        'Box Air': 'Box Air Minum',
        'Box Ayam': 'Box Vitamin Ayam',
        'Box Puyuh': 'Box Vitamin Puyuh',
        'Glodok Batok': 'Glodok Batok Kelinci',
        'Hammock': 'Hammock Sugar Glider',
        'Hand Feeder': 'Hand Feeder Burung',
        'Nipple': 'Nipple Air Minum',
        'Talang': 'Talang Pakan',
        'Bambu': 'Alas Bambu',
        'Kabel Ties': 'Kabel Ties (Cable Ties)',
        'Hook': 'Hook Gantungan',
        'Mangkok': 'Mangkok Pakan',
        'Tempat Pakan': 'Tempat Pakan Manual',
        'Jepit': 'Jepit Pakan',
    }
    
    # Check if name matches any mapping
    base_name = re.sub(r'\s*\(\d+\)$', '', name).strip()
    
    for key, value in name_mapping.items():
        if key.lower() in base_name.lower():
            return value
    
    return base_name

# Scan AKSESORIS folder
aksesoris_path = 'public/assets/image/AKSESORIS'
new_products = []

seen_names = set()

if os.path.exists(aksesoris_path):
    files = sorted(os.listdir(aksesoris_path))
    
    for file in files:
        if not file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            continue
        
        product_name = get_product_info(file)
        
        # Skip duplicates (same name)
        if product_name in seen_names:
            continue
        
        seen_names.add(product_name)
        
        product_id = create_product_id(product_name, 'aksesoris')
        
        # Create product entry
        product = {
            "id": product_id,
            "category": "Aksesoris",
            "productLine": "Aksesoris Kandang",
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
            "variants": [
                {
                    "variantName": "Standard",
                    "packageContents": ["1 Unit"],
                    "price": {
                        "min": 0,
                        "max": 0,
                        "currency": "IDR",
                        "rawText": "Hubungi Kami"
                    }
                }
            ],
            "images": [
                {
                    "sourcePdf": "Product Photo",
                    "page": 1,
                    "localPath": f"/assets/image/AKSESORIS/{file}"
                }
            ],
            "source": {
                "pdf": "Product Photo Library",
                "pages": [1],
                "rawSnippets": [product_name]
            },
            "needsReview": True,
            "outOfStock": True
        }
        
        new_products.append(product)

print(f"\nCreated {len(new_products)} unique AKSESORIS products")
print("\nSample products:")
for p in new_products[:10]:
    print(f"  - {p['id']}: {p['title']}")

# Merge with existing products
all_products = existing_products + new_products

print(f"\nTotal products: {len(existing_products)} + {len(new_products)} = {len(all_products)}")

# Save
with open('data/products.json', 'w', encoding='utf-8') as f:
    json.dump(all_products, f, ensure_ascii=False, indent=4)

print("\n✅ Updated products.json successfully!")
