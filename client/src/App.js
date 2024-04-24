import Home from './Components/home';
import ClientList from "./Components/clientList";
import AboutUs from './Components/AboutUs';

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
            <Navbar.Brand className="nav-link-custom" href="/home">Client Manager</Navbar.Brand>
            <Nav className="me-auto">
              {/* Navigation links */}
              <Nav.Link className="nav-link-custom" href="/aboutUs">About Us</Nav.Link>
              <Nav.Link className="nav-link-custom" href="/clientList">Client List</Nav.Link>
            
            </Nav>
          </Container>
        </Navbar>
          <StreamComponent></StreamComponent>>
        {/* Routes setup for different pages in the application */}
        <Routes>
          {/* Route for the home page */}
          <Route path='/home' element={<Home />}></Route>
          {/* Route for the home page (alternative path) */}
          <Route path='/clientList' element={<ClientList></ClientList>}></Route>
          {/* Route for listing tasks */}
          {/* Route for the About Us page */}
          <Route path='/aboutUs' element={<AboutUs></AboutUs>}></Route>

        </Routes>
       
      </div>
    </BrowserRouter>
    );
}

export default App;

/*return (
    <div className="App">
        

        
        <Home></Home>
        <ClientList></ClientList>

    </div>*/