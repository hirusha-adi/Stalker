import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Container from '@mui/material/Container';


// Components
import NavBar from './components/NavBar';

// Main Pages (has all the contents)
import Home from './components/home/index';
import PhoneNum from './components/phoneNum/index';


const App = () => {
  return (
    <Router>
      <NavBar />
      <Container maxWidth="md">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/phoneinfoga" element={<PhoneNum />} />
        </Routes>
      </Container>
    </Router>
  );
}

export default App;
