import React, { useContext, useRef, useState } from 'react';
import './Footer.css';
import { LodgifyContext } from '../../Context/LodgifyContext';
import { Link } from 'react-router-dom'
import check_icon from '../Assets/footer_check_icon.png';
import globe_icon from '../Assets/footer_globe_icon.png';
import facebook from '../Assets/facebook.png';
import twitter from '../Assets/twitter.png';
import instagram from '../Assets/instagram.png';

const Footer = () => {

  const [menu, setMenu] = useState("popular");
  const {inspirationListing} = useContext(LodgifyContext);
  const menuRef = useRef();

  const dropdown_toggle = (e) => {
    menuRef.current.classList.toggle('foot-menu-visible');
    e.target.classList.toggle('open');
  }

  const getLinkClass = (menuName) => {
    return menu === menuName ? 'active-link' : '';
  }


  const filteredItems = inspirationListing.filter(
    (item) => item.category === menu
  );

  return (
    <div className="footer">
      <div className="inspiration">
        <h3>Inspiration for future getaways</h3>

        <ul ref={menuRef} className="foot-inspiration-menu">
          <li
            onClick={() => {
              setMenu("popular");
            }}
          >
            <Link
              className={getLinkClass("popular")}
              style={{ textDecoration: "none" }}
              to="#"
            >
              Popular
            </Link>
            {menu === "popular" ? <hr /> : <></>}
          </li>
          <li
            onClick={() => {
              setMenu("Arts & culture");
            }}
          >
            <Link
              className={getLinkClass("Arts & culture")}
              style={{ textDecoration: "none" }}
              to="#"
            >
              Arts & culture
            </Link>
            {menu === "Arts & culture" ? <hr /> : <></>}
          </li>
          <li
            onClick={() => {
              setMenu("Outdoors");
            }}
          >
            <Link
              className={getLinkClass("Outdoors")}
              style={{ textDecoration: "none" }}
              to="#"
            >
              Outdoors
            </Link>
            {menu === "Outdoors" ? <hr /> : <></>}
          </li>
          <li
            onClick={() => {
              setMenu("Mountains");
            }}
          >
            <Link
              className={getLinkClass("Mountains")}
              style={{ textDecoration: "none" }}
              to="#"
            >
              Mountains
            </Link>
            {menu === "Mountains" ? <hr /> : <></>}
          </li>
          <li
            onClick={() => {
              setMenu("Beach");
            }}
          >
            <Link
              className={getLinkClass("Beach")}
              style={{ textDecoration: "none" }}
              to="#"
            >
              Beach
            </Link>
            {menu === "Beach" ? <hr /> : <></>}
          </li>
          <li
            onClick={() => {
              setMenu("Unique stays");
            }}
          >
            <Link
              className={getLinkClass("Unique stays")}
              style={{ textDecoration: "none" }}
              to="#"
            >
              Unique stays
            </Link>
            {menu === "Unique stays" ? <hr /> : <></>}
          </li>
          <li
            onClick={() => {
              setMenu("Categories");
            }}
          >
            <Link
              className={getLinkClass("Categories")}
              style={{ textDecoration: "none" }}
              to="#"
            >
              Categories
            </Link>
            {menu === "Categories" ? <hr /> : <></>}
          </li>
          <li
            onClick={() => {
              setMenu("Things to do");
            }}
          >
            <Link
              className={getLinkClass("Things to do")}
              style={{ textDecoration: "none" }}
              to="#"
            >
              Things to do
            </Link>
            {menu === "Things to do" ? <hr /> : <></>}
          </li>
          <li
            onClick={() => {
              setMenu("Travel tips");
            }}
          >
            <Link
              className={getLinkClass("Travel tips")}
              style={{ textDecoration: "none" }}
              to="#"
            >
              Travel tips & inspiration
            </Link>
            {menu === "Travel tips" ? <hr /> : <></>}
          </li>
          <li
            onClick={() => {
              setMenu("Lodgify-friendly");
            }}
          >
            <Link
              className={getLinkClass("Lodgify-friendly")}
              style={{ textDecoration: "none" }}
              to="#"
            >
              Lodgify-friendly apartments
            </Link>
            {menu === "Lodgify-friendly" ? <hr /> : <></>}
          </li>
        </ul>

        <hr />

        <div className="inspiration-listing">
          {filteredItems.map((item) => (
            <div key={item.id} className="inspiration-item">
              <a href="#">
                <h4>{item.name}</h4>
                <p>{item.description}</p>
              </a>
            </div>
          ))}
        </div>
      </div>

      <hr />

      <div className="support">
        <div className="support-item">
          <h4>Support</h4>
          <a href="#">Help Center</a>
          <a href="#">AirCover</a>
          <a href="#">Anti-discrimination</a>
          <a href="#">Disability support</a>
          <a href="#">Cancellations options</a>
          <a href="#">Report neighborhood concern</a>
        </div>

        <div className="support-item">
          <h4>Hosting</h4>
          <a href="#">Lodgify your home</a>
          <a href="#">AirCover for Hosts</a>
          <a href="#">Hosting resources</a>
          <a href="#">Community forum</a>
          <a href="#">Hosting responsibly</a>
          <a href="#">Lodgify-friendly apartments</a>
          <a href="#">Join a free Hosting class</a>
        </div>

        <div className="support-item">
          <h4>Lodgify</h4>
          <a href="#">Newsroom</a>
          <a href="#">New features</a>
          <a href="#">Careers</a>
          <a href="#">Investors</a>
          <a href="#">Gift cards</a>
          <a href="#">Lodgify.org emergency stays</a>
        </div>
      </div>

      <hr />

      <div className="bottom">
        <div className="privacy-section">
          <p>&copy; 2024, Lodgify Inc.</p>
          &#183;
          <p>
            <a href="#">Terms</a>
          </p>
          &#183;
          <p>
            <a href="#">Sitemap</a>
          </p>
          &#183;
          <p>
            <a href="#">Privacy</a>
          </p>
          &#183;
          <p>
            <a href="#">Your Privacy Choices</a>
          </p>
          <div className="privacy-image">
            <img src={check_icon} alt="" />
          </div>
        </div>

        <div className="socials">
          <div className="globe-image">
            <a href="#"><img src={globe_icon} alt=""/></a>
            <a href="#">English (US)</a>
          </div>

          <a href="#">NGN</a>
          <div className="images">
            <a href="#">
              <img src={facebook} alt=""/>
            </a>
          </div>
          <div className="images">
            <a href="#">
              <img src={twitter} alt=""/>
            </a>
          </div>
          <div className="images">
            <a href="#">
              <img src={instagram} alt=""/>
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Footer