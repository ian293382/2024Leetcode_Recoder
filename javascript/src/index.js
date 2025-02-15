import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import App from './App';
import Closure from './closure';
import Hosting from'./Hosting';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="/closure" element={<Closure />} />
      <Route path="/hosting" element={<Hosting />} />
      
    </Routes>
  </BrowserRouter>
);