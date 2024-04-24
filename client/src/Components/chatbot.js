import React, { useState, useEffect } from 'react';

function StreamComponent() {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const eventSource = new EventSource('http://localhost:5000/stream_response');

    eventSource.onmessage = function(event) {
      console.log('New message:', event.data);
      setMessages(prevMessages => [...prevMessages, event.data]);
    };

    eventSource.onerror = function(error) {
      console.error('EventSource failed:', error);
      eventSource.close();
    };

    return () => {
      eventSource.close();
    };
  }, []);

  return (
    <div>
      <h1>Streamed Messages</h1>
      <ul>
        {messages.map((msg, index) => (
          <li key={index}>{msg}</li>
        ))}
      </ul>
    </div>
  );
}

export default StreamComponent;
