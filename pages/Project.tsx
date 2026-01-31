import React from 'react';
import { Link } from 'react-router-dom';
import { ArrowRight, Building2, HardHat } from 'lucide-react';

const Project = () => {
    return (
        <div className="animate-fade-in">
            {/* Header */}
            <section className="bg-secondary text-white py-16">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex items-center gap-3 mb-4">
                        <Building2 size={40} className="text-primary" />
                        <h1 className="text-4xl md:text-5xl font-bold">Proyek LAQUILA</h1>
                    </div>
                    <p className="text-gray-300 text-lg max-w-3xl">
                        Menampilkan berbagai proyek dan implementasi kandang LAQUILA di berbagai peternakan di Indonesia dan mancanegara.
                    </p>
                </div>
            </section>

            {/* Content Placeholder */}
            <section className="py-16 bg-white">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="text-center max-w-2xl mx-auto">
                        <HardHat size={64} className="mx-auto text-primary mb-6" />
                        <h2 className="text-2xl font-bold text-gray-900 mb-4">Konten Sedang Disiapkan</h2>
                        <p className="text-gray-600 mb-8 leading-relaxed">
                            Halaman ini akan menampilkan berbagai proyek peternakan yang telah menggunakan produk LAQUILA,
                            termasuk studi kasus, testimoni peternak, dan dokumentasi instalasi kandang di berbagai skala usaha.
                        </p>

                        <div className="bg-orange-50 border border-orange-200 rounded-lg p-6 mb-8">
                            <h3 className="font-bold text-gray-900 mb-2">Yang Akan Ditampilkan:</h3>
                            <ul className="text-left text-gray-700 space-y-2 text-sm">
                                <li>✓ Galeri foto proyek peternakan ayam, puyuh, kelinci & burung</li>
                                <li>✓ Studi kasus implementasi kandang modular</li>
                                <li>✓ Testimoni dan review dari peternak</li>
                                <li>✓ Dokumentasi proses instalasi di berbagai wilayah</li>
                                <li>✓ Proyek custom dan spesifikasi khusus</li>
                            </ul>
                        </div>

                        <div className="flex flex-col sm:flex-row gap-4 justify-center">
                            <Link
                                to="/produk"
                                className="bg-primary hover:bg-orange-700 text-white font-bold py-3 px-6 rounded-lg flex items-center justify-center gap-2 transition-colors"
                            >
                                Lihat Katalog Produk
                                <ArrowRight size={20} />
                            </Link>
                            <Link
                                to="/hubungi-kami"
                                className="bg-white border-2 border-secondary hover:bg-gray-50 text-secondary font-bold py-3 px-6 rounded-lg flex items-center justify-center transition-colors"
                            >
                                Hubungi Kami
                            </Link>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    );
};

export default Project;
