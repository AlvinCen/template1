// Image mapping for catalog products
// This file provides image paths for all products in the catalog

// Import product data to dynamically build mappings
import { PRODUCTS } from './constants';

// Build image map dynamically from product data
const buildImageMap = (): Record<string, string> => {
    const map: Record<string, string> = {};

    for (const product of PRODUCTS) {
        // Check if product has images with localPath
        if (product.images && product.images.length > 0) {
            const firstImage = product.images[0];
            if ('localPath' in firstImage && typeof firstImage.localPath === 'string') {
                map[product.id] = firstImage.localPath;
            }
        }
    }

    return map;
};

// Product image mapping
export const PRODUCT_IMAGE_MAP = buildImageMap();

// Fallback image for products without specific mapping
export const DEFAULT_PRODUCT_IMAGE = "/assets/image/placeholder.png";

// Helper function to get product image
export const getProductImage = (productId: string): string => {
    return PRODUCT_IMAGE_MAP[productId] || DEFAULT_PRODUCT_IMAGE;
};
