import json

# Read existing products
with open('data/products.json', 'r', encoding='utf-8') as f:
    existing_products = json.load(f)

print(f"Current products: {len(existing_products)}")

# Remove the 2 products I added earlier (will re-add all 6)
existing_products = [p for p in existing_products if not p['id'].startswith('paket-panggung')]
print(f"After removing old panggung products: {len(existing_products)}")

# ALL 6 products from KANDANG PANGGUNG.pdf
new_products = [
    # 1. 4P/110 ECO
    {
        "id": "paket-panggung-4p110-eco",
        "category": "Kandang Ayam",
        "productLine": "Paket Panggung All-In",
        "title": "Paket Kandang Panggung All-In 4P/110 ECO",
        "subtitle": "Sistem panggung dengan kandang 4 pintu 110cm - ECO Series",
        "specs": {
            "material": ["Baja ringan", "Galvanis 2.2 + 2.7 + 3.4mm"],
            "finishing": ["Tanpa Powder Coating - ECO Series"],
            "capacity": ["228 - 1.032 ekor ayam"],
            "notes": ["Kandang 4 pintu 110cm, 2 ekor per pintu", "Grade 2 - ECO Series"]
        },
        "features": ["Paket lengkap termasuk bangunan", "Atap Asbes/Spandek", "Set kandang/baterai", "Talang pakan & nipple drinker", "Pipa air & box vitamin", "Penerangan listrik"],
        "variants": [
            {"variantName": "228 Ekor (7.5x5.5m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 23220000, "max": 23220000, "currency": "IDR", "rawText": "23.220.000"}},
            {"variantName": "324 Ekor (9.9x5.5m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 30840000, "max": 30840000, "currency": "IDR", "rawText": "30.840.000"}},
            {"variantName": "420 Ekor (12x5.5m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 37740000, "max": 37740000, "currency": "IDR", "rawText": "37.740.000"}},
            {"variantName": "456 Ekor (7.7x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 43860000, "max": 43860000, "currency": "IDR", "rawText": "43.860.000"}},
            {"variantName": "516 Ekor (14.3x5.5m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 45120000, "max": 45120000, "currency": "IDR", "rawText": "45.120.000"}},
            {"variantName": "552 Ekor (8.8x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 50700000, "max": 50700000, "currency": "IDR", "rawText": "50.700.000"}},
            {"variantName": "612 Ekor (16.5x5.5m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 52320000, "max": 52320000, "currency": "IDR", "rawText": "52.320.000"}},
            {"variantName": "648 Ekor (10x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 57960000, "max": 57960000, "currency": "IDR", "rawText": "57.960.000"}},
            {"variantName": "708 Ekor (18.8x5.5m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 59700000, "max": 59700000, "currency": "IDR", "rawText": "59.700.000"}},
            {"variantName": "744 Ekor (11x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 64320000, "max": 64320000, "currency": "IDR", "rawText": "64.320.000"}},
            {"variantName": "840 Ekor (12x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 70740000, "max": 70740000, "currency": "IDR", "rawText": "70.740.000"}},
            {"variantName": "936 Ekor (13.2x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 77940000, "max": 77940000, "currency": "IDR", "rawText": "77.940.000"}},
            {"variantName": "1.032 Ekor (14.3x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 84780000, "max": 84780000, "currency": "IDR", "rawText": "84.780.000"}},
        ],
        "images": [{"sourcePdf": "KANDANG PANGGUNG.pdf", "page": 4}],
        "source": {"pdf": "KANDANG PANGGUNG.pdf", "pages": [1, 4], "rawSnippets": ["4 PINTU 110 CM- ECO SERIES"]},
        "needsReview": False
    },
    # 2. 4P/110 Industrial
    {
        "id": "paket-panggung-4p110-industrial",
        "category": "Kandang Ayam",
        "productLine": "Paket Panggung All-In",
        "title": "Paket Kandang Panggung All-In 4P/110 INDUSTRIAL",
        "subtitle": "Sistem panggung dengan kandang 4 pintu 110cm - Industrial Grade",
        "specs": {
            "material": ["Baja ringan", "Galvanis 2.7 + 3.4mm"],
            "finishing": ["Powder Coating - Industrial Spec"],
            "capacity": ["228 - 1.032 ekor ayam"],
            "notes": ["Kandang 4 pintu 110cm, 2 ekor per pintu", "Grade 1 - Industrial SPEC", "Umur pakai 8-10 tahun"]
        },
        "features": ["Material Industrial Grade", "Powder Coating premium", "Umur pakai 8-10 tahun", "Investasi jangka panjang"],
        "variants": [
            {"variantName": "228 Ekor (7.5x5.5m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 24180000, "max": 24180000, "currency": "IDR", "rawText": "24.180.000"}},
            {"variantName": "324 Ekor (9.9x5.5m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 32220000, "max": 32220000, "currency": "IDR", "rawText": "32.220.000"}},
            {"variantName": "420 Ekor (12x5.5m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 39540000, "max": 39540000, "currency": "IDR", "rawText": "39.540.000"}},
            {"variantName": "456 Ekor (7.7x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 45840000, "max": 45840000, "currency": "IDR", "rawText": "45.840.000"}},
            {"variantName": "516 Ekor (14.3x5.5m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 47400000, "max": 47400000, "currency": "IDR", "rawText": "47.400.000"}},
            {"variantName": "552 Ekor (8.8x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 53040000, "max": 53040000, "currency": "IDR", "rawText": "53.040.000"}},
            {"variantName": "612 Ekor (16.5x5.5m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 54900000, "max": 54900000, "currency": "IDR", "rawText": "54.900.000"}},
            {"variantName": "648 Ekor (10x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 60670000, "max": 60670000, "currency": "IDR", "rawText": "60.670.000"}},
            {"variantName": "708 Ekor (18.8x5.5m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 62700000, "max": 62700000, "currency": "IDR", "rawText": "62.700.000"}},
            {"variantName": "744 Ekor (11x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 67500000, "max": 67500000, "currency": "IDR", "rawText": "67.500.000"}},
            {"variantName": "840 Ekor (12x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 74265000, "max": 74265000, "currency": "IDR", "rawText": "74.265.000"}},
            {"variantName": "936 Ekor (13.2x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 81900000, "max": 81900000, "currency": "IDR", "rawText": "81.900.000"}},
            {"variantName": "1.032 Ekor (14.3x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 89160000, "max": 89160000, "currency": "IDR", "rawText": "89.160.000"}},
        ],
        "images": [{"sourcePdf": "KANDANG PANGGUNG.pdf", "page": 5}],
        "source": {"pdf": "KANDANG PANGGUNG.pdf", "pages": [1, 5], "rawSnippets": ["4 PINTU 110 CM- INDUSTRIAL SPEC"]},
        "needsReview": False
    },
    # 3. 4P/120 ECO
    {
        "id": "paket-panggung-4p120-eco",
        "category": "Kandang Ayam",
        "productLine": "Paket Panggung All-In",
        "title": "Paket Kandang Panggung All-In 4P/120 ECO",
        "subtitle": "Sistem panggung dengan kandang 4 pintu 120cm - ECO Series",
        "specs": {
            "material": ["Baja ringan", "Galvanis 2.2 + 2.7 + 3.4mm"],
            "finishing": ["Tanpa Powder Coating - ECO Series"],
            "capacity": ["228 - 1.032 ekor ayam"],
            "notes": ["Kandang 4 pintu 120cm, 2 ekor per pintu", "Grade 2 - ECO Series"]
        },
        "features": ["Paket lengkap termasuk bangunan", "Kandang lebih panjang 120cm", "Set lengkap siap pakai"],
        "variants": [
            {"variantName": "228 Ekor (8x5.5m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 24780000, "max": 24780000, "currency": "IDR", "rawText": "24.780.000"}},
            {"variantName": "324 Ekor (10.5x5.5m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 32880000, "max": 32880000, "currency": "IDR", "rawText": "32.880.000"}},
            {"variantName": "420 Ekor (13x5.5m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 40800000, "max": 40800000, "currency": "IDR", "rawText": "40.800.000"}},
            {"variantName": "456 Ekor (8.2x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 46860000, "max": 46860000, "currency": "IDR", "rawText": "46.860.000"}},
            {"variantName": "516 Ekor (15.5x5.5m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 48840000, "max": 48840000, "currency": "IDR", "rawText": "48.840.000"}},
            {"variantName": "552 Ekor (9.3x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 53880000, "max": 53880000, "currency": "IDR", "rawText": "53.880.000"}},
            {"variantName": "612 Ekor (18x5.5m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 56820000, "max": 56820000, "currency": "IDR", "rawText": "56.820.000"}},
            {"variantName": "648 Ekor (10.5x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 61320000, "max": 61320000, "currency": "IDR", "rawText": "61.320.000"}},
            {"variantName": "708 Ekor (20.3x5.5m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 64440000, "max": 64440000, "currency": "IDR", "rawText": "64.440.000"}},
            {"variantName": "744 Ekor (11.8x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 69120000, "max": 69120000, "currency": "IDR", "rawText": "69.120.000"}},
            {"variantName": "840 Ekor (13x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 76540000, "max": 76540000, "currency": "IDR", "rawText": "76.540.000"}},
            {"variantName": "936 Ekor (14.2x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 83958000, "max": 83958000, "currency": "IDR", "rawText": "83.958.000"}},
            {"variantName": "1.032 Ekor (15.5x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 91800000, "max": 91800000, "currency": "IDR", "rawText": "91.800.000"}},
        ],
        "images": [{"sourcePdf": "KANDANG PANGGUNG.pdf", "page": 6}],
        "source": {"pdf": "KANDANG PANGGUNG.pdf", "pages": [1, 6], "rawSnippets": ["4 PINTU 120 CM- ECO SERIES"]},
        "needsReview": False
    },
    # 4. 4P/120 Industrial
    {
        "id": "paket-panggung-4p120-industrial",
        "category": "Kandang Ayam",
        "productLine": "Paket Panggung All-In",
        "title": "Paket Kandang Panggung All-In 4P/120 INDUSTRIAL",
        "subtitle": "Sistem panggung dengan kandang 4 pintu 120cm - Industrial Grade",
        "specs": {
            "material": ["Baja ringan", "Galvanis 2.7 + 3.4mm"],
            "finishing": ["Powder Coating - Industrial Spec"],
            "capacity": ["228 - 1.032 ekor ayam"],
            "notes": ["Kandang 4 pintu 120cm, 2 ekor per pintu", "Grade 1 - Industrial SPEC", "Umur pakai 8-10 tahun"]
        },
        "features": ["Material Industrial Grade", "Kandang lebih panjang 120cm", "Powder Coating premium"],
        "variants": [
            {"variantName": "228 Ekor (8x5.5m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 25980000, "max": 25980000, "currency": "IDR", "rawText": "25.980.000"}},
            {"variantName": "324 Ekor (10.5x5.5m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 34500000, "max": 34500000, "currency": "IDR", "rawText": "34.500.000"}},
            {"variantName": "420 Ekor (13x5.5m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 43080000, "max": 43080000, "currency": "IDR", "rawText": "43.080.000"}},
            {"variantName": "456 Ekor (8.2x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 49260000, "max": 49260000, "currency": "IDR", "rawText": "49.260.000"}},
            {"variantName": "516 Ekor (15.5x5.5m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 51600000, "max": 51600000, "currency": "IDR", "rawText": "51.600.000"}},
            {"variantName": "552 Ekor (9.3x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 56760000, "max": 56760000, "currency": "IDR", "rawText": "56.760.000"}},
            {"variantName": "612 Ekor (18x5.5m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 60000000, "max": 60000000, "currency": "IDR", "rawText": "60.000.000"}},
            {"variantName": "648 Ekor (10.5x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 64680000, "max": 64680000, "currency": "IDR", "rawText": "64.680.000"}},
            {"variantName": "708 Ekor (20.3x5.5m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 68160000, "max": 68160000, "currency": "IDR", "rawText": "68.160.000"}},
            {"variantName": "744 Ekor (11.8x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 73080000, "max": 73080000, "currency": "IDR", "rawText": "73.080.000"}},
            {"variantName": "840 Ekor (13x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 81000000, "max": 81000000, "currency": "IDR", "rawText": "81.000.000"}},
            {"variantName": "936 Ekor (14.2x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 88920000, "max": 88920000, "currency": "IDR", "rawText": "88.920.000"}},
            {"variantName": "1.032 Ekor (15.5x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 97260000, "max": 97260000, "currency": "IDR", "rawText": "97.260.000"}},
        ],
        "images": [{"sourcePdf": "KANDANG PANGGUNG.pdf", "page": 7}],
        "source": {"pdf": "KANDANG PANGGUNG.pdf", "pages": [1, 7], "rawSnippets": ["4 PINTU 120 CM- INDUSTRIAL SPEC"]},
        "needsReview": False
    },
    # 5. 6P/110 ECO
    {
        "id": "paket-panggung-6p110-eco",
        "category": "Kandang Ayam",
        "productLine": "Paket Panggung All-In",
        "title": "Paket Kandang Panggung All-In 6P/110 ECO",
        "subtitle": "Sistem panggung dengan kandang 6 pintu 110cm - ECO Series",
        "specs": {
            "material": ["Baja ringan", "Galvanis 2.2 + 2.7 + 3.4mm"],
            "finishing": ["Tanpa Powder Coating - ECO Series"],
            "capacity": ["207 - 1.062 ekor ayam"],
            "notes": ["Kandang 6 pintu 110cm, 1 ekor per pintu", "Grade 2 - ECO Series"]
        },
        "features": ["Paket lengkap termasuk bangunan", "Kandang 6 pintu lebih banyak sekat", "Cocok untuk ayam petelur"],
        "variants": [
            {"variantName": "207 Ekor (8.8x5.5m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 27900000, "max": 27900000, "currency": "IDR", "rawText": "27.900.000"}},
            {"variantName": "315 Ekor (12x5.5m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 38760000, "max": 38760000, "currency": "IDR", "rawText": "38.760.000"}},
            {"variantName": "414 Ekor (8.8x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 52020000, "max": 52020000, "currency": "IDR", "rawText": "52.020.000"}},
            {"variantName": "423 Ekor (15.5x5.5m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 50280000, "max": 50280000, "currency": "IDR", "rawText": "50.280.000"}},
            {"variantName": "531 Ekor (18.8x5.5m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 61380000, "max": 61380000, "currency": "IDR", "rawText": "61.380.000"}},
            {"variantName": "558 Ekor (11x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 66100000, "max": 66100000, "currency": "IDR", "rawText": "66.100.000"}},
            {"variantName": "603 Ekor (21x5.5m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 68760000, "max": 68760000, "currency": "IDR", "rawText": "68.760.000"}},
            {"variantName": "630 Ekor (12x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 72720000, "max": 72720000, "currency": "IDR", "rawText": "72.720.000"}},
            {"variantName": "675 Ekor (23.3x5.5m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 76380000, "max": 76380000, "currency": "IDR", "rawText": "76.380.000"}},
            {"variantName": "702 Ekor (13.2x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 80160000, "max": 80160000, "currency": "IDR", "rawText": "80.160.000"}},
            {"variantName": "846 Ekor (15.5x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 94740000, "max": 94740000, "currency": "IDR", "rawText": "94.740.000"}},
            {"variantName": "918 Ekor (16.5x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 101313000, "max": 101313000, "currency": "IDR", "rawText": "101.313.000"}},
            {"variantName": "1.062 Ekor (18.8x8.8m)", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 115860000, "max": 115860000, "currency": "IDR", "rawText": "115.860.000"}},
        ],
        "images": [{"sourcePdf": "KANDANG PANGGUNG.pdf", "page": 8}],
        "source": {"pdf": "KANDANG PANGGUNG.pdf", "pages": [1, 8], "rawSnippets": ["6 PINTU 110 CM- ECO SERIES"]},
        "needsReview": False
    },
    # 6. 6P/110 Industrial
    {
        "id": "paket-panggung-6p110-industrial",
        "category": "Kandang Ayam",
        "productLine": "Paket Panggung All-In",
        "title": "Paket Kandang Panggung All-In 6P/110 INDUSTRIAL",
        "subtitle": "Sistem panggung dengan kandang 6 pintu 110cm - Industrial Grade",
        "specs": {
            "material": ["Baja ringan", "Galvanis 2.7 + 3.4mm"],
            "finishing": ["Powder Coating - Industrial Spec"],
            "capacity": ["207 - 1.062 ekor ayam"],
            "notes": ["Kandang 6 pintu 110cm, 1 ekor per pintu", "Grade 1 - Industrial SPEC", "Umur pakai 8-10 tahun"]
        },
        "features": ["Material Industrial Grade", "Kandang 6 pintu lebih banyak sekat", "Powder Coating premium", "Investasi jangka panjang"],
        "variants": [
            {"variantName": "207 Ekor (8.8x5.5m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 29460000, "max": 29460000, "currency": "IDR", "rawText": "29.460.000"}},
            {"variantName": "315 Ekor (12x5.5m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 41100000, "max": 41100000, "currency": "IDR", "rawText": "41.100.000"}},
            {"variantName": "414 Ekor (8.8x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 55080000, "max": 55080000, "currency": "IDR", "rawText": "55.080.000"}},
            {"variantName": "423 Ekor (15.5x5.5m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 53400000, "max": 53400000, "currency": "IDR", "rawText": "53.400.000"}},
            {"variantName": "531 Ekor (18.8x5.5m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 65340000, "max": 65340000, "currency": "IDR", "rawText": "65.340.000"}},
            {"variantName": "558 Ekor (11x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 70200000, "max": 70200000, "currency": "IDR", "rawText": "70.200.000"}},
            {"variantName": "603 Ekor (21x5.5m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 73200000, "max": 73200000, "currency": "IDR", "rawText": "73.200.000"}},
            {"variantName": "630 Ekor (12x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 77400000, "max": 77400000, "currency": "IDR", "rawText": "77.400.000"}},
            {"variantName": "675 Ekor (23.3x5.5m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 81360000, "max": 81360000, "currency": "IDR", "rawText": "81.360.000"}},
            {"variantName": "702 Ekor (13.2x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 85380000, "max": 85380000, "currency": "IDR", "rawText": "85.380.000"}},
            {"variantName": "846 Ekor (15.5x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 101000000, "max": 101000000, "currency": "IDR", "rawText": "101.000.000"}},
            {"variantName": "918 Ekor (16.5x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 108000000, "max": 108000000, "currency": "IDR", "rawText": "108.000.000"}},
            {"variantName": "1.062 Ekor (18.8x8.8m)", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 123660000, "max": 123660000, "currency": "IDR", "rawText": "123.660.000"}},
        ],
        "images": [{"sourcePdf": "KANDANG PANGGUNG.pdf", "page": 9}],
        "source": {"pdf": "KANDANG PANGGUNG.pdf", "pages": [1, 9], "rawSnippets": ["6 PINTU 110 CM- INDUSTRIAL SPEC"]},
        "needsReview": False
    }
]

# Merge with existing products
all_products = existing_products + new_products

print(f"New products added: {len(new_products)}")
print(f"Total products: {len(all_products)}")

# Save updated products
with open('data/products.json', 'w', encoding='utf-8') as f:
    json.dump(all_products, f, ensure_ascii=False, indent=4)

print("\n✅ Products updated successfully!")
print("Paket Panggung products:")
for p in new_products:
    print(f"  - {p['title']} ({len(p['variants'])} variants)")
