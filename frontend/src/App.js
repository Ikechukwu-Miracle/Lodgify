import React from 'react';
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from './Components/Header/Header'
import Footer from './Components/Footer/Footer'

function App() {
  return (
    <div>
      <BrowserRouter>
	<Header />
        <Footer />
      </BrowserRouter>
    </div>
  );
}

export default App;
