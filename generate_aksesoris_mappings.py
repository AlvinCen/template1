import json
import os

# Read products to generate image mappings
with open('data/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# Generate mapping for all aksesoris products
aksesoris_mappings = []

for p in products:
    if p['category'] == 'Aksesoris' and 'images' in p and len(p['images']) > 0:
        if 'localPath' in p['images'][0]:
            image_path = p['images'][0]['localPath']
            product_id = p['id']
            aksesoris_mappings.append(f'  "{product_id}": "{image_path}",')

print("Generated image mappings for AKSESORIS:")
print(f"Total: {len(aksesoris_mappings)} products")
print("\nAdd these to productImages.ts:")
print("\n  // ===== AKSESORIS =====")
for mapping in aksesoris_mappings[:10]:
    print(mapping)
if len(aksesoris_mappings) > 10:
    print(f"  ... and {len(aksesoris_mappings) - 10} more")

# Save all mappings to file
with open('aksesoris_image_mappings.txt', 'w', encoding='utf-8') as f:
    f.write("  // ===== AKSESORIS =====\n")
    for mapping in aksesoris_mappings:
        f.write(mapping + '\n')

print(f"\n✅ Saved to aksesoris_image_mappings.txt")
