import React from 'react';
import { Heart } from 'lucide-react';

const Header = () => {
  return (
    <header className="header">
      <div className="header-content">
        <div className="logo">
          <Heart size={32} className="logo-icon" />
          <h1>Anush Cuidarte</h1>
        </div>
        <p className="subtitle">Acompañamiento integral en lactancia y crianza</p>
      </div>
    </header>
  );
};

export default Header;
