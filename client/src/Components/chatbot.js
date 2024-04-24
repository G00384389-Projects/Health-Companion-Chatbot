import React, { useState } from 'react';

function ChatBox() {
  const [userMessage, setUserMessage] = useState('');
  const [messages, setMessages] = useState([]);

  // const sendMessage = () => {
  //   if (!userMessage.trim()) return;  // Prevent sending empty messages
  //   const query = new URLSearchParams({ message: userMessage }).toString();
  //   const url = `http://localhost:5000/chat?${query}`;
  //   const eventSource = new EventSource(url);

  //   eventSource.onmessage = function(event) {
  //     console.log('New message from API:', event.data);  // Ensure this logs
  //     const newMessage = { role: 'bot', content: event.data.trim() };

  //     // Check if the message is being added to state
  //     console.log('Adding to state:', newMessage);

  //     setMessages(prevMessages => [...prevMessages, newMessage]);
  //   };

  //   eventSource.onerror = function(error) {
  //     console.error('EventSource failed:', error);
  //     eventSource.close();
  //   };

  //   // Adding user's message to the chat window immediately
  //   setMessages(prevMessages => [...prevMessages, { role: 'user', content: userMessage }]);
  //   setUserMessage('');  // Clear input after sending
  // };

  const sendMessage = () => {
    const query = new URLSearchParams({ message: userMessage }).toString();
    const url = `http://localhost:5000/chat?${query}`;
    const eventSource = new EventSource(url);

    eventSource.onmessage = function(event) {
        console.log('New message from API:', event.data);
        setMessages(prevMessages => [...prevMessages, { role: 'bot', content: event.data.trim() }]);
    };

    eventSource.onerror = function(error) {
        console.error('EventSource encountered an error:', error);
        eventSource.close();
        setMessages(prevMessages => [...prevMessages, { role: 'bot', content: "Error in connection. Please try again." }]);
    };

    setUserMessage('');
};




  return (
    <div>
      <h1>Chat with Bot</h1>
      <div className="messages">
        {messages.map((msg, index) => (
          <div key={index} className={msg.role === 'user' ? 'user' : 'bot'}>
            <strong>{msg.role === 'user' ? 'You' : 'Bot'}:</strong> {msg.content}
          </div>
        ))}
      </div>
      <input
        type="text"
        value={userMessage}
        onChange={e => setUserMessage(e.target.value)}
        onKeyPress={e => e.key === 'Enter' && sendMessage()}
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );

}

export default ChatBox;
