import React from 'react';
import { Youtube, Music, Instagram, Facebook } from 'lucide-react';
import { links } from '../data/links';

const SocialIcons = () => {
    const socialLinks = [
        { name: 'YouTube', icon: Youtube, url: links.social.youtube, color: 'hover:text-red-600' },
        { name: 'TikTok', icon: Music, url: links.social.tiktok, color: 'hover:text-black' },
        { name: 'Instagram', icon: Instagram, url: links.social.instagram, color: 'hover:text-pink-600' },
        { name: 'Facebook', icon: Facebook, url: links.social.facebook, color: 'hover:text-blue-600' },
    ];

    return (
        <div className="flex items-center gap-3">
            {socialLinks.map((social) => {
                const Icon = social.icon;
                const isDisabled = !social.url;

                if (isDisabled) {
                    return (
                        <div
                            key={social.name}
                            className="relative group"
                        >
                            <div className="w-8 h-8 flex items-center justify-center text-gray-400 cursor-not-allowed opacity-50">
                                <Icon size={18} />
                            </div>
                            <div className="absolute hidden group-hover:block bg-gray-800 text-white text-xs px-2 py-1 rounded whitespace-nowrap -bottom-8 left-1/2 transform -translate-x-1/2 z-10">
                                Link menyusul
                            </div>
                        </div>
                    );
                }

                return (
                    <a
                        key={social.name}
                        href={social.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className={`w-8 h-8 flex items-center justify-center text-gray-500 transition-colors ${social.color}`}
                        aria-label={social.name}
                    >
                        <Icon size={18} />
                    </a>
                );
            })}
        </div>
    );
};

export default SocialIcons;
