// Import React and the CSS file for styling
import React from 'react';
import './aboutUs.css';

// Define the AboutUs component
function AboutUs() {
  // JSX returned by the component
  return (
    <div className="about-container">
      <div className="about-content">

        {/* First info card: Introduction to Task Manager */}
        <div className="info-card">
       
          <div className="info-text">
            <h3>Welcome to your AI Wellness Companion</h3>
            <p>
            Your innovative companion on the journey to better health and well-being. Developed with cutting-edge 
            OpenAI technology, our chatbot is designed to assist you in self-diagnosing common health issues and 
            tracking your daily mood, supporting you to lead a healthier and more mindful life.
            </p>
          </div>
        </div>

        {/* Second info card: Mission statement */}
        <div className="info-card">
        
          <div className="info-text">
            <h3>Our Mission</h3>
            <p>
            Our mission is simple: to empower you with accessible, immediate, and personalized health insights. 
            We believe that by understanding your own health and mood patterns, you can make more informed decisions 
            about your lifestyle and well-being.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default AboutUs;
