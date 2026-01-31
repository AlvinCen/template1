import { PRODUCTS, getAllCategories, getProductsByCategory } from './data/constants.js';

console.log('='.repeat(80));
console.log('CATALOG INTEGRATION VERIFICATION');
console.log('='.repeat(80));

console.log('\n📊 Statistics:');
console.log(`Total products: ${PRODUCTS.length}`);
console.log(`Categories: ${getAllCategories().join(', ')}`);

console.log('\n📦 Products by Category:');
getAllCategories().forEach(cat => {
    const products = getProductsByCategory(cat);
    console.log(`\n${cat} (${products.length} products):`);
    products.forEach(p => {
        const prices = p.variants.map(v => v.price.min);
        const minPrice = Math.min(...prices);
        const maxPrice = Math.max(...prices);
        const priceRange = minPrice === maxPrice
            ? `Rp ${minPrice.toLocaleString('id-ID')}`
            : `Rp ${minPrice.toLocaleString('id-ID')} - Rp ${maxPrice.toLocaleString('id-ID')}`;

        console.log(`  - ${p.title} | ${priceRange} | ${p.variants.length} variant(s)`);
    });
});

console.log('\n✅ Verification complete!');
