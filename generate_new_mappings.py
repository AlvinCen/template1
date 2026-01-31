import json

# Read new products
with open('new_products_for_mapping.json', 'r', encoding='utf-8') as f:
    new_products = json.load(f)

# Generate image mappings
mappings_by_category = {}

for p in new_products:
    if 'images' in p and len(p['images']) > 0 and 'localPath' in p['images'][0]:
        category = p['category']
        if category not in mappings_by_category:
            mappings_by_category[category] = []
        
        mapping = f'  "{p["id"]}": "{p["images"][0]["localPath"]}",'
        mappings_by_category[category].append(mapping)

print(f"Generated {sum(len(v) for v in mappings_by_category.values())} image mappings\n")

# Write to file
with open('new_image_mappings.ts', 'w', encoding='utf-8') as f:
    for category, mappings in sorted(mappings_by_category.items()):
        f.write(f"\n  // ===== {category.upper()} (NEW) =====\n")
        for mapping in mappings:
            f.write(mapping + '\n')

print(f"✅ Saved to new_image_mappings.ts")
print(f"\nYou need to add these to productImages.ts")
print(f"\nSample mappings:")
for category, mappings in list(mappings_by_category.items())[:2]:
    print(f"\n{category}:")
    for mapping in mappings[:3]:
        print(mapping)
    if len(mappings) > 3:
        print(f"  ... and {len(mappings) - 3} more")
