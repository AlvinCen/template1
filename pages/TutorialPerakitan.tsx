import React from 'react';
import { Link } from 'react-router-dom';
import { ArrowRight, Video, Wrench, BookOpen } from 'lucide-react';

const TutorialPerakitan = () => {
    return (
        <div className="animate-fade-in">
            {/* Header */}
            <section className="bg-secondary text-white py-16">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex items-center gap-3 mb-4">
                        <Video size={40} className="text-primary" />
                        <h1 className="text-4xl md:text-5xl font-bold">Tutorial Perakitan Kandang</h1>
                    </div>
                    <p className="text-gray-300 text-lg max-w-3xl">
                        Panduan lengkap merakit kandang LAQUILA sistem knockdown. Mudah diikuti, tanpa perlu keahlian khusus.
                    </p>
                </div>
            </section>

            {/* Content Placeholder */}
            <section className="py-16 bg-white">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="text-center max-w-2xl mx-auto">
                        <Wrench size={64} className="mx-auto text-primary mb-6" />
                        <h2 className="text-2xl font-bold text-gray-900 mb-4">Video Tutorial Segera Hadir</h2>
                        <p className="text-gray-600 mb-8 leading-relaxed">
                            Halaman ini akan berisi video tutorial step-by-step cara merakit berbagai tipe kandang LAQUILA.
                            Sistem knockdown kami dirancang agar mudah dirakit sendiri tanpa memerlukan alat las atau keahlian khusus.
                        </p>

                        <div className="grid md:grid-cols-2 gap-6 mb-8">
                            <div className="bg-blue-50 border border-blue-200 rounded-lg p-6 text-left">
                                <div className="flex items-center gap-2 mb-3">
                                    <Video className="text-blue-600" size={24} />
                                    <h3 className="font-bold text-gray-900">Video Tutorial</h3>
                                </div>
                                <ul className="text-gray-700 space-y-2 text-sm">
                                    <li>• Cara merakit kandang ayam petelur</li>
                                    <li>• Tutorial kandang puyuh bertingkat</li>
                                    <li>• Perakitan kandang kelinci</li>
                                    <li>• Setup aviary burung</li>
                                </ul>
                            </div>

                            <div className="bg-green-50 border border-green-200 rounded-lg p-6 text-left">
                                <div className="flex items-center gap-2 mb-3">
                                    <BookOpen className="text-green-600" size={24} />
                                    <h3 className="font-bold text-gray-900">Panduan PDF</h3>
                                </div>
                                <ul className="text-gray-700 space-y-2 text-sm">
                                    <li>• Diagram perakitan detail</li>
                                    <li>• Daftar tools yang dibutuhkan</li>
                                    <li>• Tips perawatan kandang</li>
                                    <li>• Troubleshooting umum</li>
                                </ul>
                            </div>
                        </div>

                        <div className="bg-orange-50 border border-orange-200 rounded-lg p-6 mb-8">
                            <p className="text-gray-800 text-sm mb-4">
                                <strong>Catatan:</strong> Setiap pembelian kandang LAQUILA sudah dilengkapi dengan link video tutorial perakitan
                                yang akan dikirimkan via WhatsApp atau dapat diakses melalui QR code pada paket.
                            </p>
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

export default TutorialPerakitan;
