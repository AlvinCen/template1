import React from 'react';
import { Target, Heart, Wrench, Quote, History, Award } from 'lucide-react';
import { HISTORY_MILESTONES, BRANDS } from '../constants';

const About = () => {
  return (
    <div className="animate-fade-in">
      {/* Header */}
      <div className="bg-secondary text-white py-20 relative overflow-hidden">
        <div className="absolute top-0 right-0 w-64 h-64 bg-primary rounded-full blur-3xl opacity-20 -mr-16 -mt-16"></div>
        <div className="max-w-7xl mx-auto px-4 text-center relative z-10">
          <div className="inline-block bg-white/10 px-4 py-1 rounded-full text-sm font-semibold mb-4 border border-white/20">CV LAQUILA INDONESIA</div>
          <h1 className="text-4xl md:text-5xl font-bold mb-6">Workshop Project Profile</h1>
          <p className="text-xl text-gray-300 max-w-2xl mx-auto">
            Berinovasi menghadirkan kandang hewan modern, kokoh, dan memenuhi standar kesejahteraan hewan.
          </p>
        </div>
      </div>

      {/* CEO Speech */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col md:flex-row items-center gap-12">
            <div className="w-full md:w-1/3">
              <div className="relative aspect-[3/4] bg-gray-200 rounded-2xl overflow-hidden shadow-xl">
                 {/* Placeholder for CEO Image */}
                 <img src="https://picsum.photos/400/600?grayscale" alt="Imam Alfarisyi Indradi, S.ST." className="w-full h-full object-cover" />
                 <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/80 to-transparent p-6 text-white">
                   <h3 className="text-xl font-bold">Imam Alfarisyi Indradi, S.ST.</h3>
                   <p className="text-sm opacity-80">CEO Laquila Indonesia</p>
                 </div>
              </div>
            </div>
            <div className="w-full md:w-2/3">
              <div className="flex items-center gap-3 mb-6">
                 <Quote className="text-primary rotate-180" size={40} />
                 <h2 className="text-3xl font-bold text-gray-900">CEO SPEECH</h2>
              </div>
              <div className="prose prose-lg text-gray-600 space-y-6">
                <p>
                  "Sarana produksi ternak, khususnya kandang hewan yang memadai memiliki peran vital dalam menjalankan manajemen pemeliharaan agar syarat kesejahteraan hewan dapat terpenuhi, sehingga dapat menghasilkan produk ternak secara efektif dan efisien."
                </p>
                <p>
                  Karenanya <strong>Laquila</strong> hadir dan berperan aktif melakukan inovasi dalam hal penyediaan kandang hewan yang memadai, kokoh dan modern. Seluruh produk kandang yang kami produksi telah melalui proses riset, uji kelayakan serta uji pasar sehingga dapat memenuhi standar para pengguna yang berbeda atau tersegmen.
                </p>
                <p>
                   Kami berkomitmen untuk terus adaptif dalam mengakomodir segala kebutuhan para pelanggan kami. Hingga kini, produk kami sudah tersebar ke berbagai kota di Indonesia, bahkan hingga ke mancanegara."
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Vision */}
      <section className="py-16 bg-neutral">
        <div className="max-w-4xl mx-auto px-4 text-center">
          <h2 className="text-3xl font-bold text-gray-900 mb-8">Visi Kami</h2>
          <p className="text-2xl font-light text-gray-700 leading-relaxed italic">
            "Visi utama Laquila adalah tumbuh bersama para peternak dan para pecinta hewan di Indonesia."
          </p>
          <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-6">
             <div className="bg-white p-6 rounded-lg shadow-sm">
                <div className="text-primary font-bold mb-2">Adaptif & Inovatif</div>
                <p className="text-sm text-gray-500">Terus beradaptasi dengan teknologi dan kebutuhan pasar.</p>
             </div>
             <div className="bg-white p-6 rounded-lg shadow-sm">
                <div className="text-primary font-bold mb-2">Feedback Loop</div>
                <p className="text-sm text-gray-500">Mengelola analisa umpan balik pelanggan untuk pengembangan produk.</p>
             </div>
             <div className="bg-white p-6 rounded-lg shadow-sm">
                <div className="text-primary font-bold mb-2">Berbasis Komunitas</div>
                <p className="text-sm text-gray-500">Pendekatan pemasaran yang dekat dengan komunitas peternak.</p>
             </div>
          </div>
        </div>
      </section>

      {/* History Timeline */}
      <section className="py-16 bg-white">
        <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-gray-900 mb-12 text-center flex items-center justify-center gap-3">
            <History className="text-primary" /> Company History
          </h2>
          <div className="relative border-l-2 border-primary/20 ml-6 md:ml-1/2 space-y-12">
            {HISTORY_MILESTONES.map((item, idx) => (
              <div key={idx} className={`relative flex flex-col md:flex-row gap-8 ${idx % 2 === 0 ? 'md:flex-row-reverse' : ''}`}>
                <div className="absolute -left-[33px] md:left-1/2 md:-ml-[9px] w-4 h-4 rounded-full bg-primary border-4 border-white shadow-md z-10"></div>
                <div className={`ml-8 md:ml-0 md:w-1/2 ${idx % 2 === 0 ? 'md:pl-12 text-left' : 'md:pr-12 md:text-right'}`}>
                   <span className="inline-block bg-orange-100 text-primary font-bold px-3 py-1 rounded-full text-sm mb-2">
                     {item.year}
                   </span>
                   <h3 className="text-xl font-bold text-gray-900 mb-2">{item.title}</h3>
                   <p className="text-gray-600 leading-relaxed">
                     {item.description}
                   </p>
                </div>
                <div className="hidden md:block md:w-1/2"></div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Brands Strategy */}
      <section className="py-16 bg-secondary text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold mb-4">Fighter Brand Strategy</h2>
            <p className="text-gray-400 max-w-2xl mx-auto">
              Kami memahami bahwa standar pengguna sangat unik dan beragam. Kami menerapkan strategi pemasaran terarah melalui tiga pilar brand:
            </p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {BRANDS.map((brand, idx) => (
              <div key={idx} className="bg-secondary/50 border border-gray-700 p-8 rounded-xl hover:bg-gray-800 transition-colors">
                <div className={`inline-block px-3 py-1 rounded text-xs font-bold text-white mb-4 ${brand.color}`}>
                  BRAND {idx + 1}
                </div>
                <h3 className="text-2xl font-bold mb-3">{brand.name}</h3>
                <p className="text-gray-400">
                  {brand.desc}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

    </div>
  );
};

export default About;