import React from 'react';
import { Link } from 'react-router-dom';
import { FEATURED_BANNERS } from '../data/featured';

const FeaturedBanners = () => {
    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {FEATURED_BANNERS.map((banner) => (
                <Link
                    key={banner.id}
                    to={banner.hrefHash}
                    className="group relative overflow-hidden rounded-xl shadow-md hover:shadow-xl transition-all duration-300 bg-white"
                    style={{ aspectRatio: '16/9' }}
                >
                    {/* Banner Image */}
                    <img
                        src={banner.imageSrc}
                        alt={banner.title}
                        className="w-full h-full object-contain group-hover:scale-105 transition-transform duration-500"
                    />

                    {/* Overlay with Title */}
                    <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />

                    <div className="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/70 to-transparent">
                        <h3 className="text-white font-bold text-lg md:text-xl drop-shadow-lg">
                            {banner.title}
                        </h3>
                    </div>
                </Link>
            ))}
        </div>
    );
};

export default FeaturedBanners;
