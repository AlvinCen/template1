import React from 'react';
import { ShoppingCart, Check } from 'lucide-react';
import { Product } from '../types';

interface ProductCardProps {
  product: Product;
}

const ProductCard: React.FC<ProductCardProps> = ({ product }) => {
  return (
    <div className="bg-white rounded-xl shadow-sm hover:shadow-md transition-shadow duration-300 overflow-hidden flex flex-col h-full border border-gray-100">
      <div className="relative aspect-square overflow-hidden bg-gray-100">
        <img 
          src={product.imageUrl} 
          alt={product.name} 
          className="w-full h-full object-cover hover:scale-105 transition-transform duration-500"
        />
        {product.isBestSeller && (
          <div className="absolute top-3 left-3 bg-red-600 text-white text-xs font-bold px-3 py-1 rounded-full shadow-lg">
            TERLARIS
          </div>
        )}
      </div>
      
      <div className="p-5 flex flex-col flex-grow">
        <div className="text-xs font-semibold text-primary uppercase tracking-wide mb-2">
          {product.category}
        </div>
        <h3 className="text-lg font-bold text-gray-900 mb-2 line-clamp-2 leading-tight">
          {product.name}
        </h3>
        <p className="text-gray-500 text-sm mb-4 line-clamp-2 flex-grow">
          {product.description}
        </p>
        
        <div className="mb-4 space-y-1">
          {product.features.slice(0, 2).map((feat, idx) => (
            <div key={idx} className="flex items-center text-xs text-gray-600">
              <Check size={14} className="text-green-500 mr-2" />
              {feat}
            </div>
          ))}
        </div>

        <div className="pt-4 border-t border-gray-100 mt-auto">
          <div className="text-primary font-bold text-lg mb-3">
            {product.priceRange}
          </div>
          <a
            href={product.shopeeUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="w-full bg-secondary hover:bg-gray-700 text-white font-medium py-2.5 px-4 rounded-lg flex items-center justify-center gap-2 transition-colors text-sm"
          >
            <ShoppingCart size={16} />
            Beli Sekarang
          </a>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;