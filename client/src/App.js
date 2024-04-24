import Home from './Components/home';
import MoodChecker from "./Components/moodChecker";
import AboutUs from './Components/AboutUs';
import NewsList from './Components/newsList';

import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import React from 'react';
import StreamComponent from './Components/chatbot';
import "./App.css";

function App() {
   
    return (
        <BrowserRouter>
      <div className="App" >
        {/* Navbar setup using react-bootstrap components */}
        <Navbar className='navbar-custom'>
          <Container>
            <Navbar.Brand className="nav-link-custom" href="/home">AI Wellness Companion</Navbar.Brand>
            <Nav className="me-auto">
              {/* Navigation links */}
              <Nav.Link className="nav-link-custom" href="/moodChecker">Mood Checker</Nav.Link>
              <Nav.Link className="nav-link-custom" href="/aboutUs">About Us</Nav.Link>
              <Nav.Link className="nav-link-custom" href="/newsList">News LIst</Nav.Link>
            </Nav>
          </Container>
        </Navbar>
          <StreamComponent></StreamComponent>>
        {/* Routes setup for different pages in the application */}
        <Routes>
          {/* Route for the home page */}
          <Route path='/home' element={<Home />}></Route>
          {/* Route for the home page (alternative path) */}
          <Route path='/moodChecker' element={<MoodChecker></MoodChecker>}></Route>
          {/* Route for listing tasks */}
          {/* Route for the About Us page */}
          <Route path='/aboutUs' element={<AboutUs></AboutUs>}></Route>
          <Route path='/newsList' element={<NewsList></NewsList>}></Route>

        </Routes>
       
      </div>
    </BrowserRouter>
    );
}

export default App;