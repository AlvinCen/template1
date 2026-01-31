import React, { useState, useEffect } from 'react';
import { PRODUCTS as CATALOG_PRODUCTS, CATALOG_META } from '../data/constants';
import { Product as CatalogProduct } from '../data/constants';
import ProductCard from '../components/ProductCard';
import { Product } from '../types';
import { getProductImage } from '../data/productImages';

// Adapter function to convert catalog products to display format
const convertCatalogProduct = (catalogProduct: CatalogProduct): Product => {
  // Get price range from variants
  const prices = catalogProduct.variants.map(v => v.price.min);
  const minPrice = Math.min(...prices);
  const maxPrice = Math.max(...prices);
  const priceRange = minPrice === maxPrice
    ? `Rp ${minPrice.toLocaleString('id-ID')}`
    : `Rp ${minPrice.toLocaleString('id-ID')} - Rp ${maxPrice.toLocaleString('id-ID')}`;

  // Generate description from specs and features
  const description = catalogProduct.subtitle || catalogProduct.features[0] || '';

  return {
    id: catalogProduct.id,
    name: catalogProduct.title,
    priceRange: priceRange,
    category: catalogProduct.category as any,
    description: description,
    features: catalogProduct.features,
    imageUrl: getProductImage(catalogProduct.id), // Use actual product images
    shopeeUrl: `https://shopee.co.id/${CATALOG_META.brand.handles.shopee}`,
    isBestSeller: catalogProduct.productLine.includes('Baterai') || catalogProduct.productLine.includes('Carrier'),
    outOfStock: (catalogProduct as any).outOfStock || false
  };
};

const Products = () => {
  const [activeCategory, setActiveCategory] = useState<string>('Semua');
  const [displayCount, setDisplayCount] = useState(9); // Initial load: 9 products
  const [isLoading, setIsLoading] = useState(false);

  // Convert catalog products to display format
  const PRODUCTS = CATALOG_PRODUCTS.map(convertCatalogProduct);

  const categories = ['Semua', ...Array.from(new Set(PRODUCTS.map(p => p.category)))];

  const filteredProducts = activeCategory === 'Semua'
    ? PRODUCTS
    : PRODUCTS.filter(p => p.category === activeCategory);

  // Products to display (limited by displayCount)
  const displayedProducts = filteredProducts.slice(0, displayCount);
  const hasMore = displayCount < filteredProducts.length;

  // Load more products
  const loadMore = () => {
    if (isLoading || !hasMore) return;

    setIsLoading(true);
    setTimeout(() => {
      setDisplayCount(prev => prev + 6); // Load 6 more products
      setIsLoading(false);
    }, 300); // Small delay for smooth UX
  };

  // Detect scroll to bottom
  useEffect(() => {
    const handleScroll = () => {
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      const scrollHeight = document.documentElement.scrollHeight;
      const clientHeight = window.innerHeight;

      // Load more when user is 200px from bottom
      if (scrollHeight - scrollTop - clientHeight < 200 && hasMore && !isLoading) {
        loadMore();
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, [hasMore, isLoading, displayCount]);

  // Reset displayCount when category changes
  useEffect(() => {
    setDisplayCount(9);
  }, [activeCategory]);

  // Handle hash navigation from featured banners
  useEffect(() => {
    const hash = window.location.hash.substring(1);
    if (hash) {
      const categoryMap: Record<string, string> = {
        'ayam': 'Kandang Ayam',
        'puyuh': 'Kandang Puyuh',
        'burung': 'Kandang Burung & Exotic',
        'kelinci': 'Kandang Kelinci'
      };

      if (categoryMap[hash]) {
        setActiveCategory(categoryMap[hash]);
        // Smooth scroll to top after category is set
        setTimeout(() => {
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }, 100);
      }
    }
  }, []);

  return (
    <div className="bg-neutral min-h-screen py-12 animate-fade-in">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">Katalog Produk</h1>
          <p className="text-gray-600 max-w-2xl mx-auto">
            Temukan berbagai jenis kandang berkualitas untuk Ayam, Puyuh, Kelinci, Burung & Exotic.
            Material Galvanis dengan Powder Coating untuk ketahanan maksimal.
          </p>
        </div>

        {/* Category Filter with Anchor IDs */}
        <div className="flex flex-wrap justify-center gap-3 mb-10">
          <div id="ayam" className="scroll-mt-4" />
          <div id="puyuh" className="scroll-mt-4" />
          <div id="burung" className="scroll-mt-4" />
          <div id="kelinci" className="scroll-mt-4" />
          {categories.map(cat => (
            <button
              key={cat}
              onClick={() => setActiveCategory(cat)}
              className={`px-5 py-2 rounded-full text-sm font-medium transition-all ${activeCategory === cat
                ? 'bg-primary text-white shadow-md'
                : 'bg-white text-gray-600 hover:bg-gray-100 border border-gray-200'
                }`}
            >
              {cat}
            </button>
          ))}
        </div>

        {/* Products Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {displayedProducts.map(product => (
            <ProductCard key={product.id} product={product} />
          ))}
        </div>

        {/* Loading Indicator */}
        {isLoading && (
          <div className="flex justify-center items-center py-8">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-orange-500"></div>
          </div>
        )}

        {/* Load More Info */}
        {!isLoading && hasMore && (
          <div className="text-center py-8 text-gray-500">
            <p>Scroll untuk muat lebih banyak produk...</p>
            <p className="text-sm mt-2">Menampilkan {displayedProducts.length} dari {filteredProducts.length} produk</p>
          </div>
        )}

        {/* All Loaded */}
        {!hasMore && filteredProducts.length > 9 && (
          <div className="text-center py-8 text-gray-500">
            <p>✓ Semua produk telah dimuat ({filteredProducts.length} produk)</p>
          </div>
        )}

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