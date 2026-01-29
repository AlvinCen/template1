import React, { useState } from 'react';
import { PRODUCTS } from '../constants';
import ProductCard from '../components/ProductCard';

const Products = () => {
  const [activeCategory, setActiveCategory] = useState<string>('Semua');

  const categories = ['Semua', ...Array.from(new Set(PRODUCTS.map(p => p.category)))];

  const filteredProducts = activeCategory === 'Semua' 
    ? PRODUCTS 
    : PRODUCTS.filter(p => p.category === activeCategory);

  return (
    <div className="bg-neutral min-h-screen py-12 animate-fade-in">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">Katalog Produk</h1>
          <p className="text-gray-600 max-w-2xl mx-auto">
            Temukan berbagai jenis kandang ayam dan aksesoris berkualitas untuk menunjang kesuksesan peternakan Anda.
          </p>
        </div>

        {/* Category Filter */}
        <div className="flex flex-wrap justify-center gap-3 mb-10">
          {categories.map(cat => (
            <button
              key={cat}
              onClick={() => setActiveCategory(cat)}
              className={`px-5 py-2 rounded-full text-sm font-medium transition-all ${
                activeCategory === cat
                  ? 'bg-primary text-white shadow-md'
                  : 'bg-white text-gray-600 hover:bg-gray-100 border border-gray-200'
              }`}
            >
              {cat}
            </button>
          ))}
        </div>

        {/* Product Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          {filteredProducts.map(product => (
            <ProductCard key={product.id} product={product} />
          ))}
        </div>

        {filteredProducts.length === 0 && (
          <div className="text-center py-20">
            <p className="text-gray-500 text-lg">Tidak ada produk ditemukan untuk kategori ini.</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default Products;