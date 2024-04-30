import { BrowserRouter, Routes, Route } from "react-router-dom";
import './App.css'
import MainPage from './pages/mainpage/MainPage.jsx';

function App()
{
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/search" element={<MainPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App
