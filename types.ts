export interface Product {
  id: string;
  name: string;
  priceRange: string;
  category: 'Kandang Ayam' | 'Kandang Puyuh' | 'Kandang Burung & Exotic' | 'Kandang Kelinci' | 'Aksesoris';
  description: string;
  features: string[];
  imageUrl: string;
  shopeeUrl: string;
  isBestSeller?: boolean;
}

export interface Testimonial {
  id: string;
  name: string;
  content: string;
  rating: number;
}

export interface NavItem {
  label: string;
  path: string;
}

export interface HistoryEvent {
  year: string;
  title: string;
  description: string;
}