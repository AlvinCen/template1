import React, { useState } from 'react';
import { NavLink, Outlet } from 'react-router-dom';
import { Menu, X, ShoppingBag, Phone, MapPin, Instagram, ExternalLink } from 'lucide-react';
import { SHOP_INFO } from '../constants';
import SocialIcons from './SocialIcons';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const links = [
    { name: 'Home', path: '/' },
    { name: 'Produk', path: '/produk' },
    { name: 'Project', path: '/project' },
    { name: 'Tutorial Perakitan', path: '/tutorial-perakitan' },
    { name: 'Perusahaan', path: '/perusahaan' },
    { name: 'Hubungi Kami', path: '/hubungi-kami' },
  ];

  return (
    <nav className="bg-white shadow-md sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-20">
          <div className="flex items-center gap-8">
            <NavLink to="/" className="flex-shrink-0 flex items-center gap-2">
              <img src="/assets/laquila-logo.png" alt="Laquila Store" className="h-24 w-auto" />
            </NavLink>

            {/* Desktop Menu - Moved closer to logo */}
            <div className="hidden md:flex items-center space-x-4">
              {links.map((link) => (
                <NavLink
                  key={link.path}
                  to={link.path}
                  className={({ isActive }) =>
                    `text-sm font-medium transition-colors duration-200 ${isActive ? 'text-primary' : 'text-gray-500 hover:text-secondary'
                    }`
                  }
                >
                  {link.name}
                </NavLink>
              ))}
            </div>
          </div>

          {/* Right side: Social Icons and Shopee Button */}
          <div className="hidden md:flex items-center gap-3">
            <SocialIcons />

            <a
              href={SHOP_INFO.shopeeUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="bg-primary text-white px-4 py-2 rounded-full text-sm font-medium hover:bg-orange-700 transition-colors flex items-center gap-2"
            >
              <ShoppingBag size={16} />
              Buka Shopee
            </a>
          </div>

          {/* Mobile Menu Button */}
          <div className="flex items-center md:hidden">
            <button
              onClick={() => setIsOpen(!isOpen)}
              className="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-gray-500 hover:bg-gray-100 focus:outline-none"
            >
              {isOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Menu */}
      {isOpen && (
        <div className="md:hidden bg-white border-t border-gray-100">
          <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3">
            {links.map((link) => (
              <NavLink
                key={link.path}
                to={link.path}
                onClick={() => setIsOpen(false)}
                className={({ isActive }) =>
                  `block px-3 py-2 rounded-md text-base font-medium ${isActive ? 'text-primary bg-orange-50' : 'text-gray-600 hover:text-secondary hover:bg-gray-50'
                  }`
                }
              >
                {link.name}
              </NavLink>
            ))}
            <a
              href={SHOP_INFO.shopeeUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="block w-full text-center mt-4 bg-primary text-white px-4 py-2 rounded-md text-base font-medium hover:bg-orange-700"
            >
              Kunjungi Shopee
            </a>

            {/* Social Icons in mobile */}
            <div className="mt-6 flex justify-center">
              <SocialIcons />
            </div>
          </div>
        </div>
      )}
    </nav>
  );
};

const Footer = () => {
  return (
    <footer className="bg-secondary text-white pt-12 pb-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
          <div>
            <div className="flex items-center gap-2 mb-4">
              <div className="w-8 h-8 bg-primary rounded-md flex items-center justify-center text-white font-bold text-xl">
                L
              </div>
              <h3 className="text-xl font-bold">Laquila Store</h3>
            </div>
            <p className="text-gray-400 text-sm leading-relaxed mb-4">
              {SHOP_INFO.tagline}. Menyediakan kandang ayam berkualitas tinggi dengan harga pengrajin. Solusi tepat untuk memulai usaha ternak Anda.
            </p>
          </div>

          <div>
            <h4 className="text-lg font-semibold mb-4 text-orange-400">Hubungi Kami</h4>
            <ul className="space-y-3 text-gray-300 text-sm">
              <li className="flex items-start gap-3">
                <MapPin size={18} className="mt-0.5 text-primary" />
                <span>{SHOP_INFO.location}</span>
              </li>
              <li className="flex items-center gap-3">
                <Phone size={18} className="text-primary" />
                <a href={`https://wa.me/${SHOP_INFO.whatsapp}?text=${encodeURIComponent(SHOP_INFO.whatsappMessage)}`} target="_blank" rel="noreferrer" className="hover:text-white transition-colors">
                  +62 {SHOP_INFO.whatsapp.substring(2)}
                </a>
              </li>
              <li className="flex items-center gap-3">
                <ShoppingBag size={18} className="text-primary" />
                <a href={SHOP_INFO.shopeeUrl} target="_blank" rel="noreferrer" className="hover:text-white transition-colors flex items-center gap-1">
                  shopee.co.id/laquilastore1 <ExternalLink size={12} />
                </a>
              </li>
            </ul>
          </div>

          <div>
            <h4 className="text-lg font-semibold mb-4 text-orange-400">Jam Operasional</h4>
            <p className="text-gray-300 text-sm mb-2">Kami siap melayani pesanan dan konsultasi Anda pada:</p>
            <p className="font-medium text-white">{SHOP_INFO.openingHours}</p>
            <p className="text-gray-400 text-xs mt-4">Pemesanan di luar jam operasional akan diproses hari berikutnya.</p>
          </div>
        </div>

        <div className="border-t border-gray-700 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
          <p className="text-gray-500 text-sm text-center md:text-left">
            &copy; {new Date().getFullYear()} Laquila Store. All rights reserved.
          </p>
          <div className="text-gray-500 text-xs">
            Unofficial Company Profile Website
          </div>
        </div>
      </div>
    </footer>
  );
};

const Layout = () => {
  return (
    <div className="min-h-screen flex flex-col bg-neutral">
      <Navbar />
      <main className="flex-grow">
        <Outlet />
      </main>
      <Footer />
    </div>
  );
};

export default Layout;