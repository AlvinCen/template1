import React from 'react';
import { ShoppingBag, Truck, CheckCircle, MessageCircle, AlertCircle } from 'lucide-react';
import { SHOP_INFO, FAQ_ITEMS } from '../constants';

const HowToOrder = () => {
  return (
    <div className="bg-white min-h-screen animate-fade-in">
      {/* Header */}
      <div className="bg-secondary text-white py-16">
        <div className="max-w-7xl mx-auto px-4 text-center">
          <h1 className="text-3xl md:text-4xl font-bold mb-4">Cara Pemesanan</h1>
          <p className="text-gray-300 max-w-2xl mx-auto">Panduan mudah berbelanja di Laquila Store. Kami melayani pengiriman ke seluruh Indonesia.</p>
        </div>
      </div>

      <div className="max-w-4xl mx-auto px-4 py-16">
        
        {/* Steps */}
        <div className="mb-16">
          <h2 className="text-2xl font-bold text-gray-900 mb-8 text-center">Alur Pemesanan via Shopee</h2>
          <div className="relative border-l-2 border-primary/30 ml-4 md:ml-0 md:pl-0 md:border-l-0 md:grid md:grid-cols-4 md:gap-8">
            {[
              { 
                icon: <ShoppingBag />, 
                title: "1. Pilih Produk", 
                desc: "Pilih kandang sesuai kebutuhan kapasitas ternak Anda di etalase Shopee kami." 
              },
              { 
                icon: <MessageCircle />, 
                title: "2. Konfirmasi", 
                desc: "Jika ragu soal ukuran/ongkir, chat admin via Shopee/WA untuk memastikan." 
              },
              { 
                icon: <CheckCircle />, 
                title: "3. Checkout", 
                desc: "Lakukan pembayaran aman via Shopee (Bisa COD untuk area tertentu)." 
              },
              { 
                icon: <Truck />, 
                title: "4. Pengiriman", 
                desc: "Barang dikirim dalam bentuk knockdown (rakit sendiri) agar ongkir murah." 
              }
            ].map((step, idx) => (
              <div key={idx} className="mb-8 ml-8 md:ml-0 relative group">
                <div className="absolute -left-11 md:left-0 md:relative md:mb-4 w-6 h-6 bg-primary rounded-full md:mx-auto flex items-center justify-center text-white ring-4 ring-white">
                   <div className="w-2 h-2 bg-white rounded-full"></div>
                </div>
                <div className="bg-neutral p-6 rounded-xl text-center hover:bg-orange-50 transition-colors">
                  <div className="text-primary flex justify-center mb-3 md:hidden">{step.icon}</div>
                  <h3 className="font-bold text-lg mb-2">{step.title}</h3>
                  <p className="text-sm text-gray-600">{step.desc}</p>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Tips Section */}
        <div className="bg-orange-50 border border-orange-100 rounded-xl p-8 mb-16">
          <div className="flex gap-4 items-start">
            <AlertCircle className="text-primary flex-shrink-0 mt-1" size={24} />
            <div>
              <h3 className="text-lg font-bold text-gray-900 mb-2">Tips Hemat Ongkir</h3>
              <ul className="list-disc list-inside text-gray-700 space-y-2">
                <li>Gunakan <strong>Voucher Gratis Ongkir</strong> yang tersedia di Shopee.</li>
                <li>Pilih opsi pengiriman <strong>Kargo (JNE Trucking/J&T Cargo)</strong> karena kandang ayam terhitung volume besar.</li>
                <li>Jika membeli jumlah banyak (reseller), hubungi kami via WhatsApp untuk opsi ekspedisi termurah.</li>
              </ul>
            </div>
          </div>
        </div>

        {/* FAQ Section */}
        <div>
          <h2 className="text-2xl font-bold text-gray-900 mb-8 text-center">Pertanyaan Umum (FAQ)</h2>
          <div className="space-y-4">
            {FAQ_ITEMS.map((faq, idx) => (
              <div key={idx} className="border border-gray-200 rounded-lg p-5 hover:border-primary/50 transition-colors bg-white">
                <h3 className="font-bold text-gray-900 mb-2">{faq.question}</h3>
                <p className="text-gray-600">{faq.answer}</p>
              </div>
            ))}
          </div>
        </div>

      </div>
    </div>
  );
};

export default HowToOrder;