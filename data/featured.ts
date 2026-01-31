export interface FeaturedBanner {
    id: string;
    title: string;
    imageSrc: string;
    hrefHash: string;
}

export const FEATURED_BANNERS: FeaturedBanner[] = [
    {
        id: 'ayam',
        title: 'Kandang Ayam Petelur',
        imageSrc: '/assets/featured/featured-ayam.png',
        hrefHash: '/produk#ayam'
    },
    {
        id: 'puyuh',
        title: 'Kandang Puyuh Petelur',
        imageSrc: '/assets/featured/featured-puyuh.png',
        hrefHash: '/produk#puyuh'
    },
    {
        id: 'burung',
        title: 'Burung, Sugar Glider dll',
        imageSrc: '/assets/featured/featured-burung.png',
        hrefHash: '/produk#burung'
    },
    {
        id: 'kelinci',
        title: 'Kandang Kelinci',
        imageSrc: '/assets/featured/featured-kelinci.png',
        hrefHash: '/produk#kelinci'
    }
];
