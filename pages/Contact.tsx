import React from 'react';
import { Phone, MapPin, Mail, ShoppingBag } from 'lucide-react';
import { SHOP_INFO } from '../constants';

const Contact = () => {
  return (
    <div className="bg-neutral min-h-screen py-16 animate-fade-in">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h1 className="text-3xl font-bold text-gray-900 mb-4">Hubungi Kami</h1>
          <p className="text-gray-600">Punya pertanyaan seputar produk atau ingin konsultasi ukuran kandang? Tim kami siap membantu.</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
          {/* Contact Info Card */}
          <div className="bg-white rounded-2xl shadow-sm p-8">
            <h2 className="text-xl font-bold text-gray-900 mb-6 border-b pb-4">Informasi Kontak</h2>

            <div className="space-y-6">
              <a
                href={`https://wa.me/${SHOP_INFO.whatsapp}?text=${encodeURIComponent(SHOP_INFO.whatsappMessage)}`}
                target="_blank"
                rel="noreferrer"
                className="flex items-start gap-4 p-4 rounded-lg hover:bg-orange-50 transition-colors group"
              >
                <div className="w-12 h-12 bg-green-100 text-green-600 rounded-full flex items-center justify-center flex-shrink-0 group-hover:bg-green-600 group-hover:text-white transition-colors">
                  <Phone size={24} />
                </div>
                <div>
                  <h3 className="font-bold text-gray-900">WhatsApp</h3>
                  <p className="text-gray-600 text-sm mb-1">Fast Response (Chat Only)</p>
                  <p className="text-green-600 font-medium">+62 {SHOP_INFO.whatsapp.substring(2)}</p>
                </div>
              </a>

              <a
                href={SHOP_INFO.shopeeUrl}
                target="_blank"
                rel="noreferrer"
                className="flex items-start gap-4 p-4 rounded-lg hover:bg-orange-50 transition-colors group"
              >
                <div className="w-12 h-12 bg-orange-100 text-orange-600 rounded-full flex items-center justify-center flex-shrink-0 group-hover:bg-orange-600 group-hover:text-white transition-colors">
                  <ShoppingBag size={24} />
                </div>
                <div>
                  <h3 className="font-bold text-gray-900">Shopee Store</h3>
                  <p className="text-gray-600 text-sm mb-1">Order Aman & Gratis Ongkir</p>
                  <p className="text-primary font-medium">laquilastore1</p>
                </div>
              </a>

              <div className="flex items-start gap-4 p-4">
                <div className="w-12 h-12 bg-gray-100 text-gray-600 rounded-full flex items-center justify-center flex-shrink-0">
                  <MapPin size={24} />
                </div>
                <div>
                  <h3 className="font-bold text-gray-900">Lokasi Workshop</h3>
                  <p className="text-gray-600 text-sm">{SHOP_INFO.location}</p>
                  <p className="text-gray-400 text-xs mt-1">Note: Kunjungan offline wajib janjian via WA.</p>
                </div>
              </div>
            </div>
          </div>

          {/* Business Hours & Note */}
          <div className="flex flex-col gap-8">
            <div className="bg-secondary text-white rounded-2xl shadow-sm p-8">
              <h2 className="text-xl font-bold mb-4">Jam Operasional</h2>
              <div className="space-y-2">
                <div className="flex justify-between border-b border-gray-700 pb-2">
                  <span>Senin - Sabtu</span>
                  <span className="font-medium">08.00 - 17.00 WIB</span>
                </div>
                <div className="flex justify-between text-gray-400">
                  <span>Minggu</span>
                  <span>Libur (Slow Response)</span>
                </div>
              </div>
              <p className="mt-6 text-sm text-gray-300">
                Pesanan yang masuk di hari Minggu atau libur nasional akan diproses pada hari kerja berikutnya.
              </p>
            </div>

            <div className="bg-white rounded-2xl shadow-sm p-8 flex-grow flex items-center justify-center text-center">
              <div>
                <h3 className="font-bold text-gray-900 mb-2">Ingin jadi Reseller?</h3>
                <p className="text-gray-600 text-sm mb-4">
                  Dapatkan harga khusus untuk pembelian dalam jumlah banyak (partai besar) untuk dijual kembali.
                </p>
                <a
                  href={`https://wa.me/${SHOP_INFO.whatsapp}?text=Halo%20Laquila%20Store,%20saya%20tertarik%20menjadi%20reseller.`}
                  className="inline-block text-primary font-bold hover:underline"
                >
                  Hubungi Admin &rarr;
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Contact;