// App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import NavBar from './components/NavBar';
import Home from './pages/index'; // Update the path accordingly
import PhoneNumbers from './pages/phoneNum'; // Update the path accordingly

const App = () => {
  return (
    <Router>
      <div>
        <NavBar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/phone_numbers" element={<PhoneNumbers />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
