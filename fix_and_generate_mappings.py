import json

# Read all products and fix image paths
with open('data/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

fixed_count = 0

for p in products:
    if 'images' in p and len(p['images']) > 0 and 'localPath' in p['images'][0]:
        path = p['images'][0]['localPath']
        
        # Fix double path issue (e.g., "/assets/image/AYAM\Fullset.png/Fullset.png")
        if path.count('/') > 5:  # Indicates duplicate
            # Extract the correct path
            parts = path.split('\\')
            if len(parts) > 1:
                # Take everything before the last component which is the filename
                correct_path = '\\'.join(parts[:-1]).replace('\\', '/')
                p['images'][0]['localPath'] = correct_path
                fixed_count += 1

print(f"Fixed {fixed_count} image paths")

# Save fixed products
with open('data/products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=4)

print("✅ Fixed products.json")

# Generate clean image mappings
new_products = [p for p in products if p.get('outOfStock') == True]
print(f"\nGenerating mappings for {len(new_products)} out-of-stock products...")

mappings = []
for p in new_products:
    if 'images' in p and len(p['images']) > 0 and 'localPath' in p['images'][0]:
        path = p['images'][0]['localPath']
        # Ensure path uses forward slashes
        path = path.replace('\\', '/')
        mappings.append(f'  "{p["id"]}": "{path}",')

print(f"Generated {len(mappings)} mappings")

# Save to file
with open('all_new_mappings.txt', 'w', encoding='utf-8') as f:
    f.write("  // ===== NEW PRODUCTS (OUT OF STOCK) =====\n")
    for mapping in mappings:
        f.write(mapping + '\n')

print("✅ Saved to all_new_mappings.txt")
print(f"\nFirst 10 mappings:")
for mapping in mappings[:10]:
    print(mapping)
