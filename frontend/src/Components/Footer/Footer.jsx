import React, { useContext, useRef, useState } from 'react';
import './Footer.css';
import { LodgifyContext } from '../../Context/LodgifyContext';
import { Link } from 'react-router-dom'

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

        <hr/>

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

      <div className="support">Hello</div>

      <div className="bottom">World</div>
    </div>
  );
}

export default Footer