import React from 'react';
import { Shield, Sparkles, Grid3x3, Wrench, Award, Truck, Users } from 'lucide-react';
import { advantages } from '../data/content';

const AdvantagesGrid = () => {
    // Optional simple icons for each advantage
    const icons = [Shield, Sparkles, Grid3x3, Wrench, Award, Truck, Users];

    return (
        <section className="py-16 bg-neutral">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-12">
                    <h2 className="text-3xl font-bold text-gray-900">Keunggulan LAQUILA</h2>
                    <p className="mt-4 text-gray-600">Mengapa ribuan peternak mempercayai kami</p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {advantages.map((advantage, idx) => {
                        const Icon = icons[idx];
                        return (
                            <div
                                key={idx}
                                className="bg-white p-6 rounded-xl border border-gray-100 hover:shadow-lg transition-shadow group"
                            >
                                <div className="w-12 h-12 bg-orange-100 text-primary rounded-lg flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                                    <Icon size={24} />
                                </div>
                                <h3 className="text-lg font-bold text-gray-900 mb-3">{advantage.title}</h3>
                                <p className="text-gray-600 text-sm leading-relaxed">{advantage.description}</p>
                            </div>
                        );
                    })}
                </div>
            </div>
        </section>
    );
};

export default AdvantagesGrid;
