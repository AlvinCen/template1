import json
import os
from collections import defaultdict

# Read existing products
with open('data/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# Extract product identifiers from catalog
catalog_products = set()
for p in products:
    title = p['title'].lower()
    # Extract key identifiers
    if '4p/120' in title or '4p120' in title:
        catalog_products.add('4p120')
    if '4p/110' in title or '4p110' in title:
        catalog_products.add('4p110')
    if '6p/110' in title or '6p110' in title:
        catalog_products.add('6p110')
    if 'l25' in title:
        catalog_products.add('l25')
    if 'l50' in title:
        catalog_products.add('l50')
    if 'l60' in title:
        catalog_products.add('l60')
    if 'carrier' in title:
        catalog_products.add('carrier')
    if 'breeding' in title:
        catalog_products.add('breeding')
    if 'aviary' in title:
        catalog_products.add('aviary')
    if 'umbaran' in title:
        catalog_products.add('umbaran')

print("=" * 70)
print("FOTO YANG ADA TAPI BELUM JADI PRODUK DI KATALOG")
print("=" * 70)

# Check each category folder
categories = {
    'AKSESORIS': 'public/assets/image/AKSESORIS',
    'AYAM': 'public/assets/image/AYAM',
    'PUYUH': 'public/assets/image/PUYUH',
    'KELINCI': 'public/assets/image/KELINCI',
    'BURUNG': 'public/assets/image/BURUNG'
}

uncatalogued = defaultdict(list)
total_uncatalogued = 0

for cat_name, cat_path in categories.items():
    if not os.path.exists(cat_path):
        continue
    
    # Walk through directory
    for root, dirs, files in os.walk(cat_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                file_lower = file.lower()
                rel_path = os.path.relpath(os.path.join(root, file), cat_path)
                
                # Skip spec/detail images
                if 'spek' in file_lower or 'spesifikasi' in file_lower:
                    continue
                
                # Check if this product type exists in catalog
                is_catalogued = False
                
                # Special case: AKSESORIS folder - none in catalog yet
                if cat_name == 'AKSESORIS':
                    uncatalogued[cat_name].append(rel_path)
                    total_uncatalogued += 1
                    continue
                
                # Check common product identifiers
                for prod_id in catalog_products:
                    if prod_id in file_lower or prod_id in rel_path.lower():
                        is_catalogued = True
                        break
                
                if not is_catalogued:
                    # Additional checks for specific patterns
                    if cat_name == 'KELINCI':
                        if any(x in file_lower for x in ['hole', 'miring', 'carrier', 'breeding']):
                            is_catalogued = True
                    elif cat_name == 'BURUNG':
                        if any(x in file_lower for x in ['aviary', 'umbar', 'brg', 'sg']):
                            is_catalogued = True
                    
                if not is_catalogued:
                    uncatalogued[cat_name].append(rel_path)
                    total_uncatalogued += 1

# Print results
print(f"\nTotal files belum masuk katalog: {total_uncatalogued}\n")

for cat_name, files in uncatalogued.items():
    if files:
        print(f"\n📁 {cat_name}: {len(files)} files")
        # Show first 10 examples
        for f in files[:10]:
            print(f"   - {f}")
        if len(files) > 10:
            print(f"   ... dan {len(files) - 10} file lainnya")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"Total produk di katalog: {len(products)}")
print(f"Total foto di assets: 379")
print(f"Total foto belum jadi produk: {total_uncatalogued}")
print(f"Coverage: {((379 - total_uncatalogued) / 379 * 100):.1f}%")

# Breakdown potential new products
print("\n" + "=" * 70)
print("POTENSI PRODUK BARU DARI FOTO")
print("=" * 70)

print(f"\n🔧 AKSESORIS: {len(uncatalogued.get('AKSESORIS', []))} items")
print("   Kategori baru - semua aksesoris belum ada di katalog")

# Check for unique product variants in photos
print(f"\n🐔 AYAM: Foto varian/detail produk yang sudah ada")
print(f"🐦 PUYUH: Foto varian/detail produk yang sudah ada")
print(f"🐰 KELINCI: Foto varian/detail produk yang sudah ada")
print(f"🦜 BURUNG: Foto varian/detail produk yang sudah ada")
