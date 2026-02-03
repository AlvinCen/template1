import React, { useState } from 'react';
import { ArrowRight, Building2, X, ZoomIn } from 'lucide-react';
import { Link } from 'react-router-dom';

const projects = [
    { id: 2, image: '/projects/project-2.jpg', title: 'Instalasi Kandang Layer', location: 'Jawa Tengah' },
    { id: 3, image: '/projects/project-3.jpg', title: 'Automated Feeding System', location: 'Jawa Timur' },
    { id: 4, image: '/projects/project-4.jpg', title: 'Konstruksi Baja Ringan', location: 'Sumatera Utara' },
    { id: 5, image: '/projects/project-5.png', title: 'Full House Equipment', location: 'Sulawesi Selatan' },
    { id: 6, image: '/projects/project-6.png', title: 'Kandang Baterai Modern', location: 'Kalimantan Barat' },
    { id: 7, image: '/projects/project-7.png', title: 'Sistem Minum Otomatis', location: 'Jawa Barat' },
    { id: 8, image: '/projects/project-8.png', title: 'Manajemen Limbah', location: 'Bali' },
    { id: 9, image: '/projects/project-9.png', title: 'Instalasi Broiler', location: 'Lampung' },
];

const Project = () => {
    const [selectedImage, setSelectedImage] = useState<string | null>(null);

    return (
        <div className="animate-fade-in min-h-screen bg-gray-50">
            {/* Header */}
            <section className="bg-secondary text-white py-16">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex items-center gap-3 mb-4">
                        <Building2 size={40} className="text-primary" />
                        <h1 className="text-4xl md:text-5xl font-bold">Proyek LAQUILA</h1>
                    </div>
                    <p className="text-gray-300 text-lg max-w-3xl">
                        Dokumentasi proyek dan implementasi kandang modern di berbagai daerah.
                    </p>
                </div>
            </section>

            {/* Gallery Section */}
            <section className="py-12">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {projects.map((project) => (
                            <div
                                key={project.id}
                                className="group relative overflow-hidden rounded-xl shadow-lg cursor-pointer bg-white"
                                onClick={() => setSelectedImage(project.image)}
                            >
                                <div className="aspect-[4/3] overflow-hidden">
                                    <img
                                        src={project.image}
                                        alt={project.title}
                                        className="w-full h-full object-cover transform transition-transform duration-500 group-hover:scale-110"
                                    />
                                </div>
                                <div className="absolute inset-0 bg-black/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                                    <ZoomIn className="text-white w-12 h-12 opacity-80" />
                                </div>
                                <div className="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/80 to-transparent text-white transform translate-y-full group-hover:translate-y-0 transition-transform duration-300">
                                    <h3 className="font-bold text-lg">{project.title}</h3>
                                    <p className="text-sm text-gray-200">{project.location}</p>
                                </div>
                            </div>
                        ))}
                    </div>

                    {/* CTA */}
                    <div className="mt-16 text-center">
                        <h2 className="text-2xl font-bold text-gray-900 mb-4">Butuh Solusi Kandang Modern?</h2>
                        <div className="flex flex-col sm:flex-row gap-4 justify-center">
                            <Link
                                to="/produk"
                                className="bg-primary hover:bg-orange-700 text-white font-bold py-3 px-8 rounded-lg flex items-center justify-center gap-2 transition-transform hover:scale-105"
                            >
                                Lihat Produk
                                <ArrowRight size={20} />
                            </Link>
                            <Link
                                to="/hubungi-kami"
                                className="bg-white border-2 border-secondary hover:bg-gray-50 text-secondary font-bold py-3 px-8 rounded-lg flex items-center justify-center transition-transform hover:scale-105"
                            >
                                Konsultasi Gratis
                            </Link>
                        </div>
                    </div>
                </div>
            </section>

            {/* Lightbox Modal */}
            {selectedImage && (
                <div
                    className="fixed inset-0 z-50 bg-black/90 flex items-center justify-center p-4 backdrop-blur-sm animate-fade-in"
                    onClick={() => setSelectedImage(null)}
                >
                    <button
                        className="absolute top-4 right-4 text-white hover:text-primary transition-colors bg-black/50 rounded-full p-2"
                        onClick={() => setSelectedImage(null)}
                    >
                        <X size={32} />
                    </button>
                    <img
                        src={selectedImage}
                        alt="Project detailed view"
                        className="max-w-full max-h-[90vh] rounded-lg shadow-2xl"
                        onClick={(e) => e.stopPropagation()}
                    />
                </div>
            )}
        </div>
    );
};

export default Project;
