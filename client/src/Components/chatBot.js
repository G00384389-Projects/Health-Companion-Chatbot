import React, { useState, useEffect } from 'react';

function ChatBot() {
  const [assistantOutput, setAssistantOutput] = useState('');

  useEffect(() => {
    fetch('/run_assistant')
      .then(response => response.text())
      .then(data => {
        setAssistantOutput(data);
      });
  }, []);

  return (
    <div className="chat-bot">
      <h1>ChatBot</h1>
      <p>{assistantOutput}</p>
    </div>
  );
}

export default ChatBot;