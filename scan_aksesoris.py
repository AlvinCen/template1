import os
import re
import json

# Function to extract price from filename
def extract_price_from_filename(filename):
    # Look for price patterns like "10.000" or "10K" or "10k"
    price_patterns = [
        r'(\d+)\.(\d+)\.(\d+)',  # 10.000.000
        r'(\d+)\.(\d+)',          # 10.000
        r'(\d+)[kK]',             # 10k
    ]
    
    for pattern in price_patterns:
        match = re.search(pattern, filename)
        if match:
            if 'k' in pattern.lower():
                # Convert k to thousands
                return int(match.group(1)) * 1000
            else:
                # Remove dots and convert
                price_str = ''.join(match.groups())
                return int(price_str)
    return None

# Function to generate product name from filename
def generate_product_name(filename, category):
    # Remove extension
    name = os.path.splitext(filename)[0]
    
    # Remove common suffixes
    name = re.sub(r'\s*\(\d+\)$', '', name)  # Remove (2), (3), etc
    name = re.sub(r'\s+(Utama|utama).*$', '', name)  # Remove "Utama"
    name = re.sub(r'\s+\d+$', '', name)  # Remove trailing numbers
    
    # Clean up
    name = name.strip()
    
    return name

# Scan AKSESORIS folder
aksesoris_path = 'public/assets/image/AKSESORIS'
aksesoris_products = []

if os.path.exists(aksesoris_path):
    for file in os.listdir(aksesoris_path):
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            name = generate_product_name(file, 'Aksesoris')
            price = extract_price_from_filename(file)
            
            product = {
                'filename': file,
                'name': name,
                'price': price,
                'image_path': f'/assets/image/AKSESORIS/{file}'
            }
            aksesoris_products.append(product)

# Sort by name
aksesoris_products.sort(key=lambda x: x['name'])

print(f"Found {len(aksesoris_products)} AKSESORIS products")
print("\nSample products:")
for p in aksesoris_products[:20]:
    price_str = f"Rp {p['price']:,}" if p['price'] else "No price"
    print(f"  - {p['name'][:50]:50} | {price_str}")

# Save to JSON for review
with open('aksesoris_scan.json', 'w', encoding='utf-8') as f:
    json.dump(aksesoris_products, f, ensure_ascii=False, indent=2)

print(f"\n✅ Saved to aksesoris_scan.json for review")
