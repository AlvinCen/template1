import React from 'react';
import { ArrowRight, ShieldCheck, Box, Settings, Users, ShoppingBag } from 'lucide-react';
import { Link } from 'react-router-dom';
import { PRODUCTS, SHOP_INFO, TESTIMONIALS, MARKETPLACE_PARTNERS } from '../constants';
import ProductCard from '../components/ProductCard';

const Home = () => {
  const featuredProducts = PRODUCTS.filter(p => p.isBestSeller).slice(0, 3);

  return (
    <div className="animate-fade-in">
      {/* Hero Section */}
      <section className="relative bg-secondary text-white overflow-hidden">
        <div className="absolute inset-0 opacity-20 bg-[url('https://picsum.photos/1200/600?grayscale')] bg-cover bg-center" />
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 relative z-10">
          <div className="max-w-3xl">
            <div className="flex items-center gap-3 mb-4">
              <span className="bg-primary text-white text-xs font-bold px-3 py-1 rounded-full">
                CV LAQUILA INDONESIA
              </span>
              <span className="text-orange-300 font-semibold tracking-widest text-sm uppercase">
                Animal Cages Workshop
              </span>
            </div>
            <h1 className="text-4xl md:text-6xl font-extrabold tracking-tight mb-6 leading-tight">
              SiPaling <span className="text-primary">Kandang</span> <br/>
              Mengerti Kebutuhan Hewan
            </h1>
            <p className="text-lg text-gray-300 mb-8 leading-relaxed max-w-2xl">
              Pusat fabrikasi kandang hewan modern (Ayam, Puyuh, Kelinci, Burung) dengan material Galvanis & Powder Coating. Kokoh, praktis, dan teruji riset.
            </p>
            <div className="flex flex-col sm:flex-row gap-4">
              <Link to="/produk" className="bg-primary hover:bg-orange-700 text-white font-bold py-3 px-8 rounded-lg flex items-center justify-center gap-2 transition-all shadow-lg hover:shadow-orange-500/20">
                Lihat Katalog
                <ArrowRight size={20} />
              </Link>
              <Link to="/tentang" className="bg-white/10 hover:bg-white/20 backdrop-blur-sm text-white font-semibold py-3 px-8 rounded-lg flex items-center justify-center transition-all border border-white/20">
                Tentang Kami
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* USP Section */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900">Kenapa Memilih Laquila?</h2>
            <p className="mt-4 text-gray-600">Riset mendalam untuk kesejahteraan hewan dan keuntungan peternak.</p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
            {[
              { icon: <ShieldCheck size={32} />, title: "Galvanis & Powder Coating", desc: "Material anti karat ganda, awet jangka panjang & mudah dibersihkan." },
              { icon: <Settings size={32} />, title: "Sistem Knockdown", desc: "Desain segmented modern, mudah dirakit sendiri tanpa las." },
              { icon: <Box size={32} />, title: "Riset Teruji", desc: "Produk hasil riset untuk efektivitas & efisiensi operasional ternak." },
              { icon: <Users size={32} />, title: "Berbasis Komunitas", desc: "Tumbuh bersama peternak dengan layanan konsultasi responsif." },
            ].map((item, idx) => (
              <div key={idx} className="bg-neutral p-6 rounded-xl border border-gray-100 hover:shadow-md transition-shadow group hover:border-orange-200">
                <div className="w-12 h-12 bg-orange-100 text-primary rounded-lg flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                  {item.icon}
                </div>
                <h3 className="text-xl font-bold text-gray-900 mb-2">{item.title}</h3>
                <p className="text-gray-600 text-sm leading-relaxed">{item.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Marketplace Partners */}
      <section className="py-10 bg-gray-50 border-y border-gray-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <p className="text-center text-gray-500 text-sm font-semibold uppercase tracking-wider mb-6">Mitra Marketplace Resmi Kami</p>
          <div className="flex flex-wrap justify-center items-center gap-8 md:gap-16 opacity-70 grayscale hover:grayscale-0 transition-all duration-500">
             {MARKETPLACE_PARTNERS.map((partner, idx) => (
               <span key={idx} className="text-xl md:text-2xl font-bold text-gray-400 hover:text-primary cursor-default">
                 {partner}
               </span>
             ))}
          </div>
        </div>
      </section>

      {/* Featured Products */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-end mb-10">
            <div>
              <h2 className="text-3xl font-bold text-gray-900">Produk Unggulan</h2>
              <p className="mt-2 text-gray-600">Pilihan favorit peternak Ayam, Puyuh, dan Hobiis.</p>
            </div>
            <Link to="/produk" className="hidden md:flex text-primary font-semibold hover:text-orange-700 items-center gap-1">
              Lihat Semua <ArrowRight size={16} />
            </Link>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
            {featuredProducts.map(product => (
              <ProductCard key={product.id} product={product} />
            ))}
          </div>

          <div className="mt-10 text-center md:hidden">
            <Link to="/produk" className="text-primary font-semibold hover:text-orange-700 inline-flex items-center gap-1">
              Lihat Semua Produk <ArrowRight size={16} />
            </Link>
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="py-16 bg-neutral">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">Kata Mereka</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {TESTIMONIALS.map(testi => (
              <div key={testi.id} className="bg-white p-6 rounded-xl relative shadow-sm">
                <div className="text-primary text-4xl font-serif absolute top-4 left-4 opacity-20">"</div>
                <p className="text-gray-600 mb-6 relative z-10 italic">
                  {testi.content}
                </p>
                <div className="flex items-center justify-between">
                  <div className="font-bold text-gray-900">{testi.name}</div>
                  <div className="flex text-yellow-400">
                    {[...Array(5)].map((_, i) => (
                      <span key={i} className={i < testi.rating ? "text-yellow-400" : "text-gray-300"}>★</span>
                    ))}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="bg-secondary py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl font-bold text-white mb-4">Siap Memulai Ternak Anda?</h2>
          <p className="text-gray-300 mb-8 max-w-2xl mx-auto">
            Konsultasikan kebutuhan kandang spesifik Anda bersama tim Laquila.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <a 
              href={SHOP_INFO.shopeeUrl} 
              target="_blank" 
              rel="noreferrer" 
              className="bg-primary hover:bg-orange-700 text-white font-bold py-3 px-8 rounded-lg transition-colors flex items-center justify-center gap-2"
            >
              <ShoppingBag size={20} /> Order via Shopee
            </a>
            <a 
              href={`https://wa.me/${SHOP_INFO.whatsapp}`} 
              target="_blank" 
              rel="noreferrer" 
              className="bg-transparent border border-white text-white hover:bg-white hover:text-secondary font-bold py-3 px-8 rounded-lg transition-colors flex items-center justify-center gap-2"
            >
              <Users size={20} /> Chat WhatsApp
            </a>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;