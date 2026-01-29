import { Product, Testimonial, HistoryEvent } from './types';

// Informasi Toko (Updated from PDF)
export const SHOP_INFO = {
  companyName: "CV LAQUILA INDONESIA",
  name: "Laquila Store",
  tagline: "Animal Cages Workshop - SiPaling Kandang",
  whatsapp: "6285624449240",
  shopeeUrl: "https://shopee.co.id/laquilastore1",
  location: "Jawa Barat, Indonesia",
  openingHours: "Senin - Sabtu: 08.00 - 17.00 WIB",
  socialMedia: {
    youtube: "Laquila Store",
    facebook: "Laquila Store",
    instagram: "Laquila Store"
  },
  usp: [
    "Material Galvanis Anti Karat",
    "Lapisan Powder Coating",
    "Sistem Knockdown (Mudah Rakit)",
    "Riset & Pengembangan Teruji"
  ]
};

// Data Produk (Updated from PDF Catalog)
export const PRODUCTS: Product[] = [
  // KANDANG AYAM
  {
    id: "ka1",
    name: "Kandang Ayam Petelur Fullset (Galvanis + Powder Coating)",
    priceRange: "Rp 1.500.000 - Rp 2.500.000", // Estimasi harga fullset
    category: "Kandang Ayam",
    description: "Kandang ayam petelur modern dengan desain segmented yang kokoh dan praktis. Dilengkapi lapisan powder coating untuk ketahanan maksimal.",
    features: ["Material Galvanis", "Powder Coating", "Desain Modern", "Fullset Siap Pakai"],
    imageUrl: "https://picsum.photos/400/400?random=1",
    shopeeUrl: "https://shopee.co.id/laquilastore1",
    isBestSeller: true
  },
  {
    id: "ka2",
    name: "Kandang Baterai Ayam 6 Pintu",
    priceRange: "Rp 185.000 - Rp 210.000",
    category: "Kandang Ayam",
    description: "Kandang baterai efisien kapasitas 6 pintu. Lantai presisi agar telur menggelinding aman.",
    features: ["6 Pintu", "Galvanis Anti Karat", "Mudah Rakit", "Sekat Fleksibel"],
    imageUrl: "https://picsum.photos/400/400?random=2",
    shopeeUrl: "https://shopee.co.id/laquilastore1",
    isBestSeller: true
  },
  {
    id: "ka3",
    name: "Kandang Baterai Ayam 4 Pintu",
    priceRange: "Rp 135.000 - Rp 165.000",
    category: "Kandang Ayam",
    description: "Solusi hemat tempat untuk peternak skala kecil-menengah.",
    features: ["4 Pintu", "Kawat Tebal", "Standar Nasional"],
    imageUrl: "https://picsum.photos/400/400?random=3",
    shopeeUrl: "https://shopee.co.id/laquilastore1",
    isBestSeller: false
  },

  // KANDANG PUYUH
  {
    id: "kp1",
    name: "Kandang Puyuh Petelur Fullset (High Capacity)",
    priceRange: "Rp 1.200.000 - Rp 1.800.000",
    category: "Kandang Puyuh",
    description: "Rak kandang puyuh bertingkat (vertical housing) untuk efisiensi ruang maksimal. Sistem knockdown.",
    features: ["Kapasitas Besar", "Tray Kotoran", "Tempat Pakan/Minum", "Sirkulasi Udara Baik"],
    imageUrl: "https://picsum.photos/400/400?random=4",
    shopeeUrl: "https://shopee.co.id/laquilastore1",
    isBestSeller: true
  },
  {
    id: "kp2",
    name: "Kandang Puyuh Kapasitas 40-46 Ekor",
    priceRange: "Rp 150.000 - Rp 200.000",
    category: "Kandang Puyuh",
    description: "Kandang puyuh galvanis ideal untuk populasi sedang. Lantai miring untuk koleksi telur otomatis.",
    features: ["Kap 40-46 Ekor", "Galvanis", "Powder Coating Opsional"],
    imageUrl: "https://picsum.photos/400/400?random=5",
    shopeeUrl: "https://shopee.co.id/laquilastore1",
    isBestSeller: false
  },
  {
    id: "kp3",
    name: "Kandang Puyuh Kapasitas 20-26 Ekor",
    priceRange: "Rp 90.000 - Rp 120.000",
    category: "Kandang Puyuh",
    description: "Cocok untuk pemula atau skala hobi.",
    features: ["Kap 20-26 Ekor", "Ekonomis", "Praktis"],
    imageUrl: "https://picsum.photos/400/400?random=6",
    shopeeUrl: "https://shopee.co.id/laquilastore1",
    isBestSeller: false
  },

  // AVIARY & EXOTIC
  {
    id: "kb1",
    name: "Mini Aviary (Sugar Glider/Burung)",
    priceRange: "Rp 350.000 - Rp 750.000",
    category: "Kandang Burung & Exotic",
    description: "Aviary mini estetik untuk hewan kesayangan (Sugar Glider, Burung Hias). Tersedia ukuran 120x70, 120x50, 90x60.",
    features: ["Desain Luas", "Kawat Halus", "Aman untuk Kaki Hewan", "Multifungsi"],
    imageUrl: "https://picsum.photos/400/400?random=7",
    shopeeUrl: "https://shopee.co.id/laquilastore1",
    isBestSeller: false
  },
  {
    id: "kb2",
    name: "Kandang Umbaran (M/L/XL)",
    priceRange: "Rp 200.000 - Rp 400.000",
    category: "Kandang Burung & Exotic",
    description: "Kandang umbaran panjang untuk melatih pernafasan burung atau kandang koloni.",
    features: ["Size M/L/XL", "Rangka Kuat", "Mudah Dibersihkan"],
    imageUrl: "https://picsum.photos/400/400?random=8",
    shopeeUrl: "https://shopee.co.id/laquilastore1",
    isBestSeller: false
  },

  // KELINCI
  {
    id: "kk1",
    name: "Kandang Kelinci Modern Bertingkat",
    priceRange: "Rp 400.000 - Rp 800.000",
    category: "Kandang Kelinci",
    description: "Kandang kelinci higienis dengan sistem pembuangan kotoran yang baik. Tersedia model 2 tingkat dan 3 tingkat.",
    features: ["Urine Guard", "Alas Nyaman", "Anti Karat"],
    imageUrl: "https://picsum.photos/400/400?random=9",
    shopeeUrl: "https://shopee.co.id/laquilastore1",
    isBestSeller: false
  },
    {
    id: "ax1",
    name: "Nipple Drinker Automatis",
    priceRange: "Rp 3.500 - Rp 5.000",
    category: "Aksesoris",
    description: "Alat minum otomatis anti bocor.",
    features: ["Anti Bocor", "360 Derajat", "Praktis"],
    imageUrl: "https://picsum.photos/400/400?random=10",
    shopeeUrl: "https://shopee.co.id/laquilastore1",
    isBestSeller: false
  }
];

export const HISTORY_MILESTONES: HistoryEvent[] = [
  {
    year: "2010",
    title: "Awal Mula",
    description: "Berawal dari bisnis kecil keluarga dalam bidang budidaya burung puyuh untuk memanfaatkan lahan non-produktif."
  },
  {
    year: "2014",
    title: "Transformasi & Integrasi",
    description: "Bertransformasi menjadi perusahaan peternakan puyuh terintegrasi (inti-plasma, pengolahan pangan, limbah, pelatihan, eduwisata)."
  },
  {
    year: "2020",
    title: "Tantangan Pandemi",
    description: "Menjadi salah satu perusahaan yang terdampak krisis pandemi dan terpaksa menghentikan aktifitas bisnis operasional."
  },
  {
    year: "2021",
    title: "Bangkit & Rebranding",
    description: "Rebranding menjadi fabrikator kandang hewan sebagai operasi inti. Memanfaatkan digital marketing dan pendekatan berbasis komunitas."
  }
];

export const BRANDS = [
  {
    name: "LAQUILA STORE",
    desc: "Menyediakan kandang hewan untuk kebutuhan industri atau grosir dengan spesifikasi tertentu.",
    color: "bg-primary"
  },
  {
    name: "GALVA PROJECT",
    desc: "Menyediakan kebutuhan kandang hewan dengan spesifikasi umum yang sudah teruji.",
    color: "bg-blue-600"
  },
  {
    name: "KAWANI ID",
    desc: "Menyediakan kebutuhan kandang hewan dengan harga kompetitif.",
    color: "bg-green-600"
  }
];

export const MARKETPLACE_PARTNERS = [
  "Tokopedia", "Shopee", "Blibli", "Lazada", "E-Catalogue", "SiPLah"
];

export const TESTIMONIALS: Testimonial[] = [
  {
    id: "t1",
    name: "Budi Santoso",
    content: "Barang mendarat dengan aman. Rakitnya gampang banget, cuma butuh tang. Galvanisnya kelihatan tebal. Sukses terus gan.",
    rating: 5
  },
  {
    id: "t2",
    name: "Peternak Maju",
    content: "Kandang baterainya presisi, telur langsung gelinding ke depan jadi nggak keinjek ayam. Seller ramah via chat.",
    rating: 5
  },
  {
    id: "t3",
    name: "Rina Wati",
    content: "Pengiriman cepat. Untuk harga segini kualitasnya oke banget buat pemula seperti saya.",
    rating: 4
  }
];

export const FAQ_ITEMS = [
  {
    question: "Apakah kandang dikirim dalam keadaan sudah dirakit?",
    answer: "Tidak. Kandang dikirim dalam kondisi belum dirakit (knockdown) untuk menghemat ongkos kirim. Kami menyertakan video tutorial perakitan yang mudah diikuti."
  },
  {
    question: "Apa keunggulan material Galvanis & Powder Coating?",
    answer: "Kawat galvanis tahan karat, ditambah lapisan powder coating membuat kandang jauh lebih awet, tahan goresan, dan mudah dibersihkan dari kotoran ternak."
  },
  {
    question: "Berapa lama pengiriman barang?",
    answer: "Pesanan sebelum jam 14.00 WIB dikirim hari yang sama. Kami mendukung pengiriman via Kargo (JNE/J&T) agar ongkir lebih murah untuk barang besar."
  },
  {
    question: "Apakah ada garansi?",
    answer: "Wajib video unboxing. Kami menjamin barang dikirim dalam kondisi baik. Kerusakan pengiriman dapat diklaim melalui fitur komplain marketplace."
  }
];