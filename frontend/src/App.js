import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Footer from './Components/Footer/Footer'

function App() {
  return (
    <div>
      <BrowserRouter>
        <Footer />
      </BrowserRouter>
    </div>
  );
}

export default App;
