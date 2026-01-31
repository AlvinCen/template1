import json

# Read existing products
with open('data/products.json', 'r', encoding='utf-8') as f:
    existing_products = json.load(f)

print(f"Current products: {len(existing_products)}")

# ALL MISSING PRODUCTS
missing_products = [
    # ===== FROM KATALOG AYAM =====
    # 1. Paket Fullset Indus 2 Tingkat Tipe A
    {
        "id": "paket-fullset-indus-2-tingkat-tipe-a",
        "category": "Kandang Ayam",
        "productLine": "Paket Fullset Industrial",
        "title": "Paket Fullset Industrial 2 Tingkat Tipe A",
        "subtitle": "Paket lengkap dengan rangka 2 tingkat tipe A",
        "specs": {
            "material": ["Galvanis 2.7 + 3.4mm", "Besi Beton 12-16mm"],
            "finishing": ["Powder Coating - Industrial Spec"],
            "capacity": ["16-24 ekor (2 tingkat)"],
            "rangka": ["2 Tingkat", "Besi Beton 12-16mm"],
            "notes": ["Industrial Grade", "Paket siap rakit"]
        },
        "features": ["Rangka kokoh 2 tingkat", "Material Industrial Grade", "Paket lengkap siap rakit"],
        "variants": [
            {"variantName": "4P/120", "packageContents": ["2 Unit Baterai 4P/120", "Rangka 2 tingkat", "Aksesoris lengkap"], "price": {"min": 750000, "max": 750000, "currency": "IDR", "rawText": "750.000"}},
            {"variantName": "4P/110", "packageContents": ["2 Unit Baterai 4P/110", "Rangka 2 tingkat", "Aksesoris lengkap"], "price": {"min": 800000, "max": 800000, "currency": "IDR", "rawText": "800.000"}},
            {"variantName": "6P/110", "packageContents": ["2 Unit Baterai 6P/110", "Rangka 2 tingkat", "Aksesoris lengkap"], "price": {"min": 820000, "max": 820000, "currency": "IDR", "rawText": "820.000"}},
        ],
        "images": [{"sourcePdf": "Katalog & Price List Ayam.pdf", "page": 7}],
        "source": {"pdf": "Katalog & Price List Ayam.pdf", "pages": [7], "rawSnippets": ["PAKET FULLSET INDUS 2 TINGKAT TIPE A"]},
        "needsReview": False
    },
    # 2. Paket Fullset Indus 2 Tingkat Tipe B
    {
        "id": "paket-fullset-indus-2-tingkat-tipe-b",
        "category": "Kandang Ayam",
        "productLine": "Paket Fullset Industrial",
        "title": "Paket Fullset Industrial 2 Tingkat Tipe B",
        "subtitle": "Paket lengkap dengan rangka 2 tingkat tipe B",
        "specs": {
            "material": ["Galvanis 2.7 + 3.4mm", "Besi Beton 12-16mm"],
            "finishing": ["Powder Coating - Industrial Spec"],
            "capacity": ["16-24 ekor (2 tingkat)"],
            "rangka": ["2 Tingkat", "Besi Beton 12-16mm"],
            "notes": ["Industrial Grade", "Paket siap rakit"]
        },
        "features": ["Rangka kokoh 2 tingkat", "Material Industrial Grade", "Paket lengkap siap rakit"],
        "variants": [
            {"variantName": "4P/120", "packageContents": ["2 Unit Baterai 4P/120", "Rangka 2 tingkat", "Aksesoris lengkap"], "price": {"min": 890000, "max": 890000, "currency": "IDR", "rawText": "890.000"}},
            {"variantName": "4P/110", "packageContents": ["2 Unit Baterai 4P/110", "Rangka 2 tingkat", "Aksesoris lengkap"], "price": {"min": 930000, "max": 930000, "currency": "IDR", "rawText": "930.000"}},
            {"variantName": "6P/110", "packageContents": ["2 Unit Baterai 6P/110", "Rangka 2 tingkat", "Aksesoris lengkap"], "price": {"min": 950000, "max": 950000, "currency": "IDR", "rawText": "950.000"}},
        ],
        "images": [{"sourcePdf": "Katalog & Price List Ayam.pdf", "page": 8}],
        "source": {"pdf": "Katalog & Price List Ayam.pdf", "pages": [8], "rawSnippets": ["PAKET FULLSET INDUS 2 TINGKAT TIPE B"]},
        "needsReview": False
    },
    # 3. Paket Fullset Indus 2 Tingkat Tipe C
    {
        "id": "paket-fullset-indus-2-tingkat-tipe-c",
        "category": "Kandang Ayam",
        "productLine": "Paket Fullset Industrial",
        "title": "Paket Fullset Industrial 2 Tingkat Tipe C",
        "subtitle": "Paket lengkap dengan rangka 2 tingkat tipe C",
        "specs": {
            "material": ["Galvanis 2.7 + 3.4mm", "Besi Beton 12-16mm"],
            "finishing": ["Powder Coating - Industrial Spec"],
            "capacity": ["16-24 ekor (2 tingkat)"],
            "rangka": ["2 Tingkat", "Besi Beton 12-16mm"],
            "notes": ["Industrial Grade", "Paket siap rakit"]
        },
        "features": ["Rangka kokoh 2 tingkat", "Material Industrial Grade", "Paket lengkap siap rakit"],
        "variants": [
            {"variantName": "4P/120", "packageContents": ["2 Unit Baterai 4P/120", "Rangka 2 tingkat", "Aksesoris lengkap"], "price": {"min": 1280000, "max": 1280000, "currency": "IDR", "rawText": "1.280.000"}},
            {"variantName": "4P/110", "packageContents": ["2 Unit Baterai 4P/110", "Rangka 2 tingkat", "Aksesoris lengkap"], "price": {"min": 1350000, "max": 1350000, "currency": "IDR", "rawText": "1.350.000"}},
            {"variantName": "6P/110", "packageContents": ["2 Unit Baterai 6P/110", "Rangka 2 tingkat", "Aksesoris lengkap"], "price": {"min": 1370000, "max": 1370000, "currency": "IDR", "rawText": "1.370.000"}},
        ],
        "images": [{"sourcePdf": "Katalog & Price List Ayam.pdf", "page": 9}],
        "source": {"pdf": "Katalog & Price List Ayam.pdf", "pages": [9], "rawSnippets": ["PAKET FULLSET INDUS 2 TINGKAT TIPE C"]},
        "needsReview": False
    },
    # 4. Paket Fullset Indus 3 Tingkat
    {
        "id": "paket-fullset-indus-3-tingkat",
        "category": "Kandang Ayam",
        "productLine": "Paket Fullset Industrial",
        "title": "Paket Fullset Industrial 3 Tingkat",
        "subtitle": "Paket lengkap dengan rangka 3 tingkat",
        "specs": {
            "material": ["Galvanis 2.7 + 3.4mm", "Besi Beton 12-16mm"],
            "finishing": ["Powder Coating - Industrial Spec"],
            "capacity": ["24-36 ekor (3 tingkat)"],
            "rangka": ["3 Tingkat", "Besi Beton 12-16mm"],
            "notes": ["Industrial Grade", "Paket siap rakit"]
        },
        "features": ["Rangka kokoh 3 tingkat", "Material Industrial Grade", "Kapasitas lebih besar"],
        "variants": [
            {"variantName": "4P/120", "packageContents": ["3 Unit Baterai 4P/120", "Rangka 3 tingkat", "Aksesoris lengkap"], "price": {"min": 1490000, "max": 1490000, "currency": "IDR", "rawText": "1.490.000"}},
            {"variantName": "4P/110", "packageContents": ["3 Unit Baterai 4P/110", "Rangka 3 tingkat", "Aksesoris lengkap"], "price": {"min": 1570000, "max": 1570000, "currency": "IDR", "rawText": "1.570.000"}},
            {"variantName": "6P/110", "packageContents": ["3 Unit Baterai 6P/110", "Rangka 3 tingkat", "Aksesoris lengkap"], "price": {"min": 1590000, "max": 1590000, "currency": "IDR", "rawText": "1.590.000"}},
        ],
        "images": [{"sourcePdf": "Katalog & Price List Ayam.pdf", "page": 10}],
        "source": {"pdf": "Katalog & Price List Ayam.pdf", "pages": [10], "rawSnippets": ["PAKET FULLSET INDUS 3 TINGKAT"]},
        "needsReview": False
    },
    # 5. Paket Fullset Indus 3 Tingkat + Box
    {
        "id": "paket-fullset-indus-3-tingkat-box",
        "category": "Kandang Ayam",
        "productLine": "Paket Fullset Industrial",
        "title": "Paket Fullset Industrial 3 Tingkat + Box",
        "subtitle": "Paket lengkap dengan rangka 3 tingkat dan box vitamin",
        "specs": {
            "material": ["Galvanis 2.7 + 3.4mm", "Besi Beton 12-16mm"],
            "finishing": ["Powder Coating - Industrial Spec"],
            "capacity": ["24-36 ekor (3 tingkat)"],
            "rangka": ["3 Tingkat", "Besi Beton 12-16mm"],
            "notes": ["Industrial Grade", "Include box vitamin", "Paket siap rakit"]
        },
        "features": ["Rangka kokoh 3 tingkat", "Material Industrial Grade", "Include box vitamin", "Paket paling lengkap"],
        "variants": [
            {"variantName": "4P/120", "packageContents": ["3 Unit Baterai 4P/120", "Rangka 3 tingkat", "Box vitamin", "Aksesoris lengkap"], "price": {"min": 1695000, "max": 1695000, "currency": "IDR", "rawText": "1.695.000"}},
            {"variantName": "4P/110", "packageContents": ["3 Unit Baterai 4P/110", "Rangka 3 tingkat", "Box vitamin", "Aksesoris lengkap"], "price": {"min": 1840000, "max": 1840000, "currency": "IDR", "rawText": "1.840.000"}},
            {"variantName": "6P/110", "packageContents": ["3 Unit Baterai 6P/110", "Rangka 3 tingkat", "Box vitamin", "Aksesoris lengkap"], "price": {"min": 1860000, "max": 1860000, "currency": "IDR", "rawText": "1.860.000"}},
        ],
        "images": [{"sourcePdf": "Katalog & Price List Ayam.pdf", "page": 11}],
        "source": {"pdf": "Katalog & Price List Ayam.pdf", "pages": [11], "rawSnippets": ["PAKET FULLSET INDUS 3 TINGKAT + BOX"]},
        "needsReview": False
    },
    
    # ===== FROM KATALOG PUYUH =====
    # 6. Fullset 200 Ekor Rangka Hollow
    {
        "id": "fullset-puyuh-200-ekor-rangka-hollow",
        "category": "Kandang Puyuh",
        "productLine": "Fullset dengan Rangka",
        "title": "Fullset Puyuh 200 Ekor Rangka Hollow",
        "subtitle": "Paket fullset 200 ekor dengan rangka hollow",
        "specs": {
            "material": ["Galvanis 2.2, 2.7 & 3.4mm"],
            "finishing": ["Powder Coating"],
            "capacity": ["200 ekor puyuh"],
            "rangka": ["Hollow 1.5x3cm galvanis"],
            "notes": ["Ringan & harga ekonomis", "Proses perakitan praktis"]
        },
        "features": ["Rangka hollow ringan", "Paket lengkap untuk 200 ekor", "Harga ekonomis"],
        "variants": [
            {"variantName": "TLG Komplit P1", "packageContents": ["Baterai L50 TLG", "Rangka Hollow", "Talang pakan", "Nipple P1", "Aksesoris lengkap"], "price": {"min": 1520000, "max": 1520000, "currency": "IDR", "rawText": "1.520.000"}},
            {"variantName": "TLG Komplit A9", "packageContents": ["Baterai L50 TLG", "Rangka Hollow", "Talang pakan", "Nipple A9", "Aksesoris lengkap"], "price": {"min": 1940000, "max": 1940000, "currency": "IDR", "rawText": "1.940.000"}},
            {"variantName": "OTO Komplit P1", "packageContents": ["Baterai L50 OTO", "Rangka Hollow", "Tempat pakan otomatis", "Nipple P1", "Aksesoris lengkap"], "price": {"min": 1720000, "max": 1720000, "currency": "IDR", "rawText": "1.720.000"}},
            {"variantName": "OTO Komplit A9", "packageContents": ["Baterai L50 OTO", "Rangka Hollow", "Tempat pakan otomatis", "Nipple A9", "Aksesoris lengkap"], "price": {"min": 2140000, "max": 2140000, "currency": "IDR", "rawText": "2.140.000"}},
        ],
        "images": [{"sourcePdf": "Katalog & Price List PUYUH.pdf", "page": 7}],
        "source": {"pdf": "Katalog & Price List PUYUH.pdf", "pages": [7], "rawSnippets": ["FULLSET 200 EKOR RANGKA HOLLOW"]},
        "needsReview": False
    },
    # 7. Fullset 200 Ekor Rangka Siku
    {
        "id": "fullset-puyuh-200-ekor-rangka-siku",
        "category": "Kandang Puyuh",
        "productLine": "Fullset dengan Rangka",
        "title": "Fullset Puyuh 200 Ekor Rangka Siku",
        "subtitle": "Paket fullset 200 ekor dengan rangka siku (rekomendasi)",
        "specs": {
            "material": ["Galvanis 2.2, 2.7 & 3.4mm"],
            "finishing": ["Powder Coating"],
            "capacity": ["200 ekor puyuh"],
            "rangka": ["Siku 4x4cm powder coating"],
            "notes": ["Kokoh, kuat dan tahan lama", "RECOMMENDED"]
        },
        "features": ["Rangka siku kokoh (rekomendasi)", "Paket lengkap untuk 200 ekor", "Tahan lama"],
        "variants": [
            {"variantName": "TLG Komplit P1", "packageContents": ["Baterai L50 TLG", "Rangka Siku", "Talang pakan", "Nipple P1", "Aksesoris lengkap"], "price": {"min": 1785000, "max": 1785000, "currency": "IDR", "rawText": "1.785.000"}},
            {"variantName": "TLG Komplit A9", "packageContents": ["Baterai L50 TLG", "Rangka Siku", "Talang pakan", "Nipple A9", "Aksesoris lengkap"], "price": {"min": 2390000, "max": 2390000, "currency": "IDR", "rawText": "2.390.000"}},
            {"variantName": "OTO Komplit P1", "packageContents": ["Baterai L50 OTO", "Rangka Siku", "Tempat pakan otomatis", "Nipple P1", "Aksesoris lengkap"], "price": {"min": 1950000, "max": 1950000, "currency": "IDR", "rawText": "1.950.000"}},
            {"variantName": "OTO Komplit A9", "packageContents": ["Baterai L50 OTO", "Rangka Siku", "Tempat pakan otomatis", "Nipple A9", "Aksesoris lengkap"], "price": {"min": 2520000, "max": 2520000, "currency": "IDR", "rawText": "2.520.000"}},
        ],
        "images": [{"sourcePdf": "Katalog & Price List PUYUH.pdf", "page": 8}],
        "source": {"pdf": "Katalog & Price List PUYUH.pdf", "pages": [8], "rawSnippets": ["FULLSET 200 EKOR RANGKA SIKU"]},
        "needsReview": False
    },
    # 8. Fullset 250 Ekor Rangka Hollow
    {
        "id": "fullset-puyuh-250-ekor-rangka-hollow",
        "category": "Kandang Puyuh",
        "productLine": "Fullset dengan Rangka",
        "title": "Fullset Puyuh 250 Ekor Rangka Hollow",
        "subtitle": "Paket fullset 250 ekor dengan rangka hollow",
        "specs": {
            "material": ["Galvanis 2.2, 2.7 & 3.4mm"],
            "finishing": ["Powder Coating"],
            "capacity": ["250 ekor puyuh"],
            "rangka": ["Hollow 1.5x3cm galvanis"],
            "notes": ["Ringan & harga ekonomis", "Proses perakitan praktis"]
        },
        "features": ["Rangka hollow ringan", "Paket lengkap untuk 250 ekor", "Harga ekonomis"],
        "variants": [
            {"variantName": "TLG Komplit P1", "packageContents": ["Baterai L50 TLG", "Rangka Hollow", "Talang pakan", "Nipple P1", "Aksesoris lengkap"], "price": {"min": 1630000, "max": 1630000, "currency": "IDR", "rawText": "1.630.000"}},
            {"variantName": "TLG Komplit A9", "packageContents": ["Baterai L50 TLG", "Rangka Hollow", "Talang pakan", "Nipple A9", "Aksesoris lengkap"], "price": {"min": 2050000, "max": 2050000, "currency": "IDR", "rawText": "2.050.000"}},
            {"variantName": "OTO Komplit P1", "packageContents": ["Baterai L50 OTO", "Rangka Hollow", "Tempat pakan otomatis", "Nipple P1", "Aksesoris lengkap"], "price": {"min": 1840000, "max": 1840000, "currency": "IDR", "rawText": "1.840.000"}},
            {"variantName": "OTO Komplit A9", "packageContents": ["Baterai L50 OTO", "Rangka Hollow", "Tempat pakan otomatis", "Nipple A9", "Aksesoris lengkap"], "price": {"min": 2260000, "max": 2260000, "currency": "IDR", "rawText": "2.260.000"}},
        ],
        "images": [{"sourcePdf": "Katalog & Price List PUYUH.pdf", "page": 9}],
        "source": {"pdf": "Katalog & Price List PUYUH.pdf", "pages": [9], "rawSnippets": ["FULLSET 250 EKOR RANGKA HOLLOW"]},
        "needsReview": False
    },
    # 9. Fullset 250 Ekor Rangka Siku
    {
        "id": "fullset-puyuh-250-ekor-rangka-siku",
        "category": "Kandang Puyuh",
        "productLine": "Fullset dengan Rangka",
        "title": "Fullset Puyuh 250 Ekor Rangka Siku",
        "subtitle": "Paket fullset 250 ekor dengan rangka siku (rekomendasi)",
        "specs": {
            "material": ["Galvanis 2.2, 2.7 & 3.4mm"],
            "finishing": ["Powder Coating"],
            "capacity": ["250 ekor puyuh"],
            "rangka": ["Siku 4x4cm powder coating"],
            "notes": ["Kokoh, kuat dan tahan lama", "RECOMMENDED"]
        },
        "features": ["Rangka siku kokoh (rekomendasi)", "Paket lengkap untuk 250 ekor", "Tahan lama"],
        "variants": [
            {"variantName": "TLG Komplit P1", "packageContents": ["Baterai L50 TLG", "Rangka Siku", "Talang pakan", "Nipple P1", "Aksesoris lengkap"], "price": {"min": 1900000, "max": 1900000, "currency": "IDR", "rawText": "1.900.000"}},
            {"variantName": "TLG Komplit A9", "packageContents": ["Baterai L50 TLG", "Rangka Siku", "Talang pakan", "Nipple A9", "Aksesoris lengkap"], "price": {"min": 2500000, "max": 2500000, "currency": "IDR", "rawText": "2.500.000"}},
            {"variantName": "OTO Komplit P1", "packageContents": ["Baterai L50 OTO", "Rangka Siku", "Tempat pakan otomatis", "Nipple P1", "Aksesoris lengkap"], "price": {"min": 2040000, "max": 2040000, "currency": "IDR", "rawText": "2.040.000"}},
            {"variantName": "OTO Komplit A9", "packageContents": ["Baterai L50 OTO", "Rangka Siku", "Tempat pakan otomatis", "Nipple A9", "Aksesoris lengkap"], "price": {"min": 2640000, "max": 2640000, "currency": "IDR", "rawText": "2.640.000"}},
        ],
        "images": [{"sourcePdf": "Katalog & Price List PUYUH.pdf", "page": 10}],
        "source": {"pdf": "Katalog & Price List PUYUH.pdf", "pages": [10], "rawSnippets": ["FULLSET 250 EKOR RANGKA SIKU"]},
        "needsReview": False
    }
]

# Merge with existing products
all_products = existing_products + missing_products

print(f"Missing products added: {len(missing_products)}")
print(f"Total products now: {len(all_products)}")

# Save updated products
with open('data/products.json', 'w', encoding='utf-8') as f:
    json.dump(all_products, f, ensure_ascii=False, indent=4)

print("\n✅ All missing products added successfully!")
print("\nProduct breakdown:")
for p in missing_products:
    print(f"  - {p['title']} ({len(p['variants'])} variants)")
