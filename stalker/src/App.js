import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import NavBar from './components/NavBar';
import Home from './pages/index';
import PhoneNumbers from './pages/phoneNum';
import Container from '@mui/material/Container';

const App = () => {
  return (
    <Router>
      <NavBar />
      <Container maxWidth="md">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/phone_numbers" element={<PhoneNumbers />} />
        </Routes>
      </Container>
    </Router>
  );
}

export default App;
