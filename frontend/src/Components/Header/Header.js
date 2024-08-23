import React from 'react';
import './Header.css';
import { FaSearch, FaGlobe, FaBars, FaUserCircle } from 'react-icons/fa';

function Header() {
  return (
    <header className="header">
      {/* Logo Section */}
      <div className="header__logo">
        <img
          src="https://res.cloudinary.com/dy2aom8f0/image/upload/w_1000,c_fill,ar_1:1,g_auto,r_max,bo_5px_solid_red,b_rgb:262c35/v1723304345/Pink_and_Black_Modern_Initials_Logo_Design__3_-removebg-preview_d7cs7a.png"
          alt="Logo"
        />
      </div>

      {/* Search Section */}
      <div className="header__search">
        <div className="search__categories">
          <button className="category__button">Available</button>
          <button className="category__button">Experience</button>
        </div>
        <div className="search__inputs">
          <input type="text" placeholder="Location" className="search__input" />
          <input type="date" placeholder="Arrival" className="search__input" />
          <input type="date" placeholder="Departure" className="search__input" />
          <input 
            type="number" 
            placeholder="Guest Members" 
            className="search__input" 
            min="1" 
          />
        </div>
        <button className="search__button">
          <FaSearch />
        </button>
      </div>

      {/* Right Section */}
      <div className="header__right">
        <a href="#" className="header__link">Lodgify, Home Anywhere</a>
        <FaGlobe className="header__icon" />
        <div className="header__profile">
          <FaBars className="header__icon" />
          <FaUserCircle className="header__icon" />
        </div>
      </div>
    </header>
  );
}

export default Header;
