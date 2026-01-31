// Test script to verify image loading
import { PRODUCTS } from './data/constants';
import { getProductImage, PRODUCT_IMAGE_MAP } from './data/productImages';

console.log('Testing Product Images...\n');

// Check first 10 products
const testProducts = PRODUCTS.slice(0, 10);

testProducts.forEach(p => {
    const imagePath = getProductImage(p.id);
    const hasImage = p.images && p.images.length > 0;
    const localPath = hasImage && 'localPath' in p.images[0] ? p.images[0].localPath : 'NONE';

    console.log(`\nProduct: ${p.id}`);
    console.log(`  Title: ${p.title}`);
    console.log(`  Has images: ${hasImage}`);
    console.log(`  LocalPath: ${localPath}`);
    console.log(`  Mapped path: ${imagePath}`);
    console.log(`  In map: ${p.id in PRODUCT_IMAGE_MAP}`);
});

console.log(`\n\nTotal products: ${PRODUCTS.length}`);
console.log(`Total in image map: ${Object.keys(PRODUCT_IMAGE_MAP).length}`);
