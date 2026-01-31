import json

# Read products.json
with open('data/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# Read catalog_meta.json
with open('data/catalog_meta.json', 'r', encoding='utf-8') as f:
    catalog_meta = json.load(f)

# Generate TypeScript constants file
ts_content = '''// Auto-generated catalog constants from PDF extraction
// Generated: 2026-01-30
// Total products: ''' + str(len(products)) + '''

export interface Price {
  min: number;
  max: number;
  currency: string;
  rawText: string;
}

export interface ProductVariant {
  variantName: string;
  productCode?: string;
  packageContents: string[];
  price: Price;
}

export interface ImageReference {
  sourcePdf: string;
  page: number;
  caption?: string;
}

export interface ProductSource {
  pdf: string;
  pages: number[];
  rawSnippets: string[];
}

export interface ProductSpecs {
  material?: string[];
  finishing?: string[];
  dimensions?: string[];
  capacity?: string[];
  gridSpacing?: string[];
  notes?: string[];
}

export interface Product {
  id: string;
  category: string;
  productLine: string;
  title: string;
  subtitle?: string;
  specs: ProductSpecs;
  features: string[];
  variants: ProductVariant[];
  images: ImageReference[];
  source: ProductSource;
  needsReview: boolean;
}

export interface CatalogMeta {
  brand: {
    name: string;
    tagline: string;
    whatsapp: string;
    handles: {
      shopee: string;
    };
  };
  globalSellingPoints: string[];
  notes: string[];
}

export const CATALOG_META: CatalogMeta = ''' + json.dumps(catalog_meta, indent=2) + ''';

export const PRODUCTS: Product[] = ''' + json.dumps(products, indent=2) + ''';

// Helper functions for filtering and searching
export const getProductsByCategory = (category: string): Product[] => {
  return PRODUCTS.filter(p => p.category === category);
};

export const getProductById = (id: string): Product | undefined => {
  return PRODUCTS.find(p => p.id === id);
};

export const getAllCategories = (): string[] => {
  return Array.from(new Set(PRODUCTS.map(p => p.category)));
};

export const getProductsNeedingReview = (): Product[] => {
  return PRODUCTS.filter(p => p.needsReview);
};
'''

# Write to constants.ts
with open('data/constants.ts', 'w', encoding='utf-8') as f:
    f.write(ts_content)

print(f"✅ constants.ts updated successfully!")
print(f"Total products exported: {len(products)}")
print(f"Categories: {', '.join(set(p['category'] for p in products))}")
