import React, { useEffect } from 'react';
import { HashRouter, Routes, Route, useLocation } from 'react-router-dom';
import Layout from './components/Layout';
import Home from './pages/Home';
import Products from './pages/Products';
import HowToOrder from './pages/HowToOrder';
import About from './pages/About';
import Contact from './pages/Contact';

// Scroll to top helper
const ScrollToTop = () => {
  const { pathname } = useLocation();
  useEffect(() => {
    window.scrollTo(0, 0);
  }, [pathname]);
  return null;
};

const App = () => {
  return (
    <HashRouter>
      <ScrollToTop />
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="produk" element={<Products />} />
          <Route path="cara-pesan" element={<HowToOrder />} />
          <Route path="tentang" element={<About />} />
          <Route path="kontak" element={<Contact />} />
        </Route>
      </Routes>
    </HashRouter>
  );
};

export default App;