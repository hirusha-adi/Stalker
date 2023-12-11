// react
import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

// mui
import Container from "@mui/material/Container";

// my components
import NavBar from "./components/NavBar";

// my pages
import Home from "./components/home/index";
import PhoneNum from "./components/phoneNum/index";
import AccountCheck from "./components/accountCheck/index";

const App = () => {
  return (
    <Router>
      <NavBar />
      <Container maxWidth="md">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/phoneinfoga" element={<PhoneNum />} />
          <Route path="/sherlock" element={<AccountCheck />} />
        </Routes>
      </Container>
    </Router>
  );
};

export default App;
