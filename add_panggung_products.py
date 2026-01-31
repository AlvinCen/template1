import json

# Read existing products
with open('data/products.json', 'r', encoding='utf-8') as f:
    existing_products = json.load(f)

print(f"Existing products: {len(existing_products)}")

# New products from KANDANG PANGGUNG.pdf
new_products = [
    {
        "id": "paket-panggung-4p110-eco-228-ekor",
        "category": "Kandang Ayam",
        "productLine": "Paket Panggung All-In",
        "title": "Paket Kandang Panggung All-In 4P/110 ECO 228 Ekor",
        "subtitle": "Sistem panggung lengkap dengan bangunan",
        "specs": {
            "material": ["Baja ringan", "Galvanis 2.2 + 2.7 + 3.4mm"],
            "finishing": ["Tanpa Powder Coating - ECO Series"],
            "dimensions": ["Bangunan: 7.5 x 5.5 m"],
            "capacity": ["228 ekor ayam"],
            "notes": ["Kandang 4 pintu 110cm, 2 ekor per pintu"]
        },
        "features": [
            "Paket lengkap dengan struktur bangunan",
            "Atap Asbes/Spandek",
            "Set kandang/baterai lengkap",
            "Set talang pakan & nipple drinker",
            "Set pipa air & box vitamin",
            "Set penerangan listrik",
            "Cukup siapin lokasi, kami bangun sampai siap huni"
        ],
        "variants": [
            {"variantName": "228 Ekor 7.5x5.5m", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 23220000, "max": 23220000, "currency": "IDR", "rawText": "23.220.000"}},
            {"variantName": "324 Ekor 9.9x5.5m", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 30840000, "max": 30840000, "currency": "IDR", "rawText": "30.840.000"}},
            {"variantName": "420 Ekor 12x5.5m", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 37740000, "max": 37740000, "currency": "IDR", "rawText": "37.740.000"}},
            {"variantName": "516 Ekor 14.3x5.5m", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 45120000, "max": 45120000, "currency": "IDR", "rawText": "45.120.000"}},
            {"variantName": "552 Ekor 8.8x8.8m", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 50700000, "max": 50700000, "currency": "IDR", "rawText": "50.700.000"}},
            {"variantName": "612 Ekor 16.5x5.5m", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 52320000, "max": 52320000, "currency": "IDR", "rawText": "52.320.000"}},
            {"variantName": "648 Ekor 10x8.8m", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 57960000, "max": 57960000, "currency": "IDR", "rawText": "57.960.000"}},
            {"variantName": "708 Ekor 18.8x5.5m", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 59700000, "max": 59700000, "currency": "IDR", "rawText": "59.700.000"}},
            {"variantName": "744 Ekor 11x8.8m", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 64320000, "max": 64320000, "currency": "IDR", "rawText": "64.320.000"}},
            {"variantName": "840 Ekor 12x8.8m", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 70740000, "max": 70740000, "currency": "IDR", "rawText": "70.740.000"}},
            {"variantName": "936 Ekor 13.2x8.8m", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 77940000, "max": 77940000, "currency": "IDR", "rawText": "77.940.000"}},
            {"variantName": "1.032 Ekor 14.3x8.8m", "packageContents": ["Struktur bangunan", "Baterai", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 84780000, "max": 84780000, "currency": "IDR", "rawText": "84.780.000"}},
        ],
        "images": [{"sourcePdf": "KANDANG PANGGUNG.pdf", "page": 4}],
        "source": {"pdf": "KANDANG PANGGUNG.pdf", "pages": [1, 4], "rawSnippets": ["PAKET KANDANG PANGGUNG ALL IN", "4 PINTU 110 CM- ECO SERIES"]},
        "needsReview": False
    },
    {
        "id": "paket-panggung-4p110-industrial-228-ekor",
        "category": "Kandang Ayam",
        "productLine": "Paket Panggung All-In",
        "title": "Paket Kandang Panggung All-In 4P/110 INDUSTRIAL 228 Ekor",
        "subtitle": "Sistem panggung lengkap dengan bangunan - Industrial Grade",
        "specs": {
            "material": ["Baja ringan", "Galvanis 2.7 + 3.4mm"],
            "finishing": ["Powder Coating - Industrial Spec"],
            "dimensions": ["Bangunan: 7.5 x 5.5 m"],
            "capacity": ["228 ekor ayam"],
            "notes": ["Kandang 4 pintu 110cm, 2 ekor per pintu", "Grade 1 - Industrial SPEC"]
        },
        "features": [
            "Paket lengkap dengan struktur bangunan",
            "Material Industrial Grade dengan Powder Coating",
            "Umur pakai 8-10 tahun",
            "Investasi jangka panjang",
            "Cukup siapin lokasi, kami bangun sampai siap huni"
        ],
        "variants": [
            {"variantName": "228 Ekor 7.5x5.5m", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 24180000, "max": 24180000, "currency": "IDR", "rawText": "24.180.000"}},
            {"variantName": "324 Ekor 9.9x5.5m", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 32220000, "max": 32220000, "currency": "IDR", "rawText": "32.220.000"}},
            {"variantName": "420 Ekor 12x5.5m", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 39540000, "max": 39540000, "currency": "IDR", "rawText": "39.540.000"}},
            {"variantName": "516 Ekor 14.3x5.5m", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 47400000, "max": 47400000, "currency": "IDR", "rawText": "47.400.000"}},
            {"variantName": "552 Ekor 8.8x8.8m", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 53040000, "max": 53040000, "currency": "IDR", "rawText": "53.040.000"}},
            {"variantName": "612 Ekor 16.5x5.5m", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 54900000, "max": 54900000, "currency": "IDR", "rawText": "54.900.000"}},
            {"variantName": "648 Ekor 10x8.8m", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 60670000, "max": 60670000, "currency": "IDR", "rawText": "60.670.000"}},
            {"variantName": "708 Ekor 18.8x5.5m", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 62700000, "max": 62700000, "currency": "IDR", "rawText": "62.700.000"}},
            {"variantName": "744 Ekor 11x8.8m", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 67500000, "max": 67500000, "currency": "IDR", "rawText": "67.500.000"}},
            {"variantName": "840 Ekor 12x8.8m", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 74265000, "max": 74265000, "currency": "IDR", "rawText": "74.265.000"}},
            {"variantName": "936 Ekor 13.2x8.8m", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 81900000, "max": 81900000, "currency": "IDR", "rawText": "81.900.000"}},
            {"variantName": "1.032 Ekor 14.3x8.8m", "packageContents": ["Struktur bangunan", "Baterai Industrial", "Talang pakan", "Nipple drinker", "Pipa air", "Box vitamin", "Penerangan"], "price": {"min": 89160000, "max": 89160000, "currency": "IDR", "rawText": "89.160.000"}},
        ],
        "images": [{"sourcePdf": "KANDANG PANGGUNG.pdf", "page": 5}],
        "source": {"pdf": "KANDANG PANGGUNG.pdf", "pages": [1, 5], "rawSnippets": ["PAKET KANDANG PANGGUNG ALL IN", "4 PINTU 110 CM- INDUSTRIAL SPEC"]},
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
print(f"File: data/products.json")
