import React, { useEffect } from 'react';
import { HashRouter, Routes, Route, useLocation } from 'react-router-dom';
import Layout from './components/Layout';
import Home from './pages/Home';
import Products from './pages/Products';
import HowToOrder from './pages/HowToOrder';
import About from './pages/About';
import Contact from './pages/Contact';
import Project from './pages/Project';
import TutorialPerakitan from './pages/TutorialPerakitan';

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
          <Route path="project" element={<Project />} />
          <Route path="tutorial-perakitan" element={<TutorialPerakitan />} />
          <Route path="perusahaan" element={<About />} />
          <Route path="hubungi-kami" element={<Contact />} />

          {/* Legacy routes for backwards compatibility */}
          <Route path="tentang" element={<About />} />
          <Route path="kontak" element={<Contact />} />
          <Route path="cara-pesan" element={<HowToOrder />} />
        </Route>
      </Routes>
    </HashRouter>
  );
};

export default App;