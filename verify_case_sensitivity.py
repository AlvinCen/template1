import json
import os

# Helper to find actual proper-cased filename
def get_actual_case(path):
    directory, filename = os.path.split(path)
    if not os.path.exists(directory):
        return None
    
    # List files in directory
    files = os.listdir(directory)
    
    # Check for exact match first
    if filename in files:
        return os.path.join(directory, filename)
    
    # Check for case-insensitive match
    lower_filename = filename.lower()
    for f in files:
        if f.lower() == lower_filename:
            return os.path.join(directory, f)
            
    return None

# Load products
with open('data/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

print("Checking case sensitivity for Vercel deployment...")
print("-" * 50)

fixed_count = 0
issues = 0

for p in products:
    if 'images' in p and len(p['images']) > 0 and 'localPath' in p['images'][0]:
        # Path in JSON (e.g., /assets/image/AYAM/foo.png)
        json_path = p['images'][0]['localPath']
        
        # Convert to filesystem path (e.g., public/assets/image/AYAM/foo.png)
        # Remove leading slash for os.path.join
        rel_path = json_path.lstrip('/')
        fs_path = os.path.join('public', rel_path)
        
        # Get directory and filename
        directory = os.path.dirname(fs_path)
        filename = os.path.basename(fs_path)
        
        if not os.path.exists(directory):
            print(f"❌ Directory not found: {directory}")
            issues += 1
            continue
            
        # Check if file exists with exact casing
        if filename not in os.listdir(directory):
            # File might exist with different casing, let's find it
            actual_path = get_actual_case(fs_path)
            
            if actual_path:
                # Construct the correct localPath
                # Remove 'public' and ensure forward slashes
                correct_rel_path = actual_path.replace('public\\', '').replace('public/', '').replace('\\', '/')
                correct_json_path = '/' + correct_rel_path
                
                print(f"⚠️  Case Mismatch: {p['id']}")
                print(f"   Current: {json_path}")
                print(f"   Fixed:   {correct_json_path}")
                
                p['images'][0]['localPath'] = correct_json_path
                fixed_count += 1
            else:
                print(f"❌ File not found (any case): {fs_path}")
                issues += 1
        else:
            # Exact match, good!
            pass

print("-" * 50)
if fixed_count > 0:
    print(f"Fixed {fixed_count} case sensitivity issues.")
    # Save changes
    with open('data/products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)
    print("✅ products.json updated.")
else:
    print("✅ All paths match filesystem casing exactly.")

if issues > 0:
    print(f"❌ Found {issues} critical issues (files not found).")
