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

            {/* Video Tutorials Section */}
            <section className="py-16 bg-gray-50">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="text-center mb-12">
                        <h2 className="text-3xl font-bold text-gray-900 mb-4">Video Tutorial Perakitan</h2>
                        <p className="text-gray-600 text-lg max-w-3xl mx-auto">
                            Panduan lengkap step-by-step cara merakit berbagai tipe kandang LAQUILA.
                            Sistem knockdown kami dirancang agar mudah dirakit sendiri tanpa memerlukan alat las atau keahlian khusus.
                        </p>
                    </div>

                    {/* Video Grid */}
                    <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                        {/* Kandang Ayam */}
                        <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow">
                            <div className="aspect-video">
                                <iframe
                                    className="w-full h-full"
                                    src="https://www.youtube.com/embed/YC7K_mRu6NA"
                                    title="Tutorial Perakitan Kandang Ayam"
                                    frameBorder="0"
                                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                                    allowFullScreen
                                ></iframe>
                            </div>
                            <div className="p-6">
                                <h3 className="font-bold text-xl text-gray-900 mb-2">Kandang Ayam</h3>
                                <p className="text-gray-600 text-sm">Tutorial perakitan kandang ayam petelur sistem knockdown</p>
                            </div>
                        </div>

                        {/* Kandang Puyuh */}
                        <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow">
                            <div className="aspect-video">
                                <iframe
                                    className="w-full h-full"
                                    src="https://www.youtube.com/embed/4rfXBwkg2Lg"
                                    title="Tutorial Perakitan Kandang Puyuh"
                                    frameBorder="0"
                                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                                    allowFullScreen
                                ></iframe>
                            </div>
                            <div className="p-6">
                                <h3 className="font-bold text-xl text-gray-900 mb-2">Kandang Puyuh</h3>
                                <p className="text-gray-600 text-sm">Tutorial perakitan kandang puyuh bertingkat</p>
                            </div>
                        </div>

                        {/* Kandang SG/Burung */}
                        <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow">
                            <div className="aspect-video">
                                <iframe
                                    className="w-full h-full"
                                    src="https://www.youtube.com/embed/mFqST-qPREc"
                                    title="Tutorial Perakitan Kandang SG/Burung"
                                    frameBorder="0"
                                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                                    allowFullScreen
                                ></iframe>
                            </div>
                            <div className="p-6">
                                <h3 className="font-bold text-xl text-gray-900 mb-2">Kandang SG/Burung</h3>
                                <p className="text-gray-600 text-sm">Tutorial perakitan kandang SG/burung</p>
                            </div>
                        </div>

                        {/* Mini Aviary */}
                        <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow">
                            <div className="aspect-video">
                                <iframe
                                    className="w-full h-full"
                                    src="https://www.youtube.com/embed/TBOFl42A9As"
                                    title="Tutorial Perakitan Mini Aviary"
                                    frameBorder="0"
                                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                                    allowFullScreen
                                ></iframe>
                            </div>
                            <div className="p-6">
                                <h3 className="font-bold text-xl text-gray-900 mb-2">Mini Aviary</h3>
                                <p className="text-gray-600 text-sm">Tutorial perakitan mini aviary untuk burung</p>
                            </div>
                        </div>

                        {/* Kandang Kelinci */}
                        <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow">
                            <div className="aspect-video">
                                <iframe
                                    className="w-full h-full"
                                    src="https://www.youtube.com/embed/WXK1vb9rreE"
                                    title="Tutorial Perakitan Kandang Kelinci"
                                    frameBorder="0"
                                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                                    allowFullScreen
                                ></iframe>
                            </div>
                            <div className="p-6">
                                <h3 className="font-bold text-xl text-gray-900 mb-2">Kandang Kelinci</h3>
                                <p className="text-gray-600 text-sm">Tutorial perakitan kandang kelinci</p>
                            </div>
                        </div>

                        {/* Pet Carrier */}
                        <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow">
                            <div className="aspect-video">
                                <iframe
                                    className="w-full h-full"
                                    src="https://www.youtube.com/embed/N9GGfjedFaU"
                                    title="Tutorial Perakitan Pet Carrier"
                                    frameBorder="0"
                                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                                    allowFullScreen
                                ></iframe>
                            </div>
                            <div className="p-6">
                                <h3 className="font-bold text-xl text-gray-900 mb-2">Pet Carrier</h3>
                                <p className="text-gray-600 text-sm">Tutorial perakitan pet carrier</p>
                            </div>
                        </div>
                    </div>

                    {/* Info Section */}
                    <div className="mt-12 max-w-4xl mx-auto">
                        <div className="bg-orange-50 border border-orange-200 rounded-lg p-6 mb-8">
                            <div className="flex items-start gap-3">
                                <BookOpen className="text-orange-600 mt-1" size={24} />
                                <div>
                                    <h3 className="font-bold text-gray-900 mb-2">Catatan Penting</h3>
                                    <p className="text-gray-800 text-sm">
                                        Setiap pembelian kandang LAQUILA sudah dilengkapi dengan link video tutorial perakitan
                                        yang akan dikirimkan via WhatsApp atau dapat diakses melalui QR code pada paket.
                                    </p>
                                </div>
                            </div>
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
