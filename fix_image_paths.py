import json
import os
import re

# Read products
with open('data/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

fixed_count = 0
issues_found = []

for p in products:
    if 'images' in p and len(p['images']) > 0 and 'localPath' in p['images'][0]:
        original_path = p['images'][0]['localPath']
        fixed_path = original_path
        
        # Fix 1: Remove duplicate filename at end
        # e.g., "/assets/image/AYAM/Fullset.png/Fullset.png" -> "/assets/image/AYAM/Fullset.png"
        parts = fixed_path.split('/')
        if len(parts) > 2:
            # Check if last two parts are the same (indicating duplicate)
            if parts[-1] == parts[-2] or (parts[-1] in parts[-2]):
                fixed_path = '/'.join(parts[:-1])
                fixed_count += 1
        
        # Fix 2: Convert backslashes to forward slashes
        if '\\' in fixed_path:
            fixed_path = fixed_path.replace('\\', '/')
            fixed_count += 1
        
        # Fix 3: Ensure path starts with /assets
        if not fixed_path.startswith('/assets'):
            if fixed_path.startswith('assets'):
                fixed_path = '/' + fixed_path
            else:
                issues_found.append(f"{p['id']}: Invalid path - {fixed_path}")
        
        # Update if changed
        if fixed_path != original_path:
            p['images'][0]['localPath'] = fixed_path
            print(f"Fixed: {p['id']}")
            print(f"  From: {original_path}")
            print(f"  To:   {fixed_path}")

print(f"\n{'='*60}")
print(f"Fixed {fixed_count} image paths")
print(f"Issues found: {len(issues_found)}")

if issues_found:
    print("\nPaths with issues:")
    for issue in issues_found[:10]:
        print(f"  - {issue}")

# Save fixed products
with open('data/products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=4)

print("\n✅ Saved fixed products.json")

# Verify paths exist
print("\nVerifying file existence...")
missing = []
for p in products:
    if 'images' in p and len(p['images']) > 0 and 'localPath' in p['images'][0]:
        path = p['images'][0]['localPath']
        # Convert to filesystem path
        fs_path = 'public' + path
        if not os.path.exists(fs_path):
            missing.append(f"{p['id']}: {path}")

print(f"Missing files: {len(missing)}")
if missing:
    print("\nFirst 10 missing:")
    for m in missing[:10]:
        print(f"  - {m}")
