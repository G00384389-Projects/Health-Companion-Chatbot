import React, { useState } from 'react';

function ChatBot() {
  const [output, setOutput] = useState('');

  const runPythonScript = () => {
    fetch('/callassistant')
      .then(response => response.json())
      .then(data => {
        if (data.error) {
          setOutput('Error: ' + data.error);
        } else {
          setOutput(data.output);
        }
      })
      .catch(error => {
        setOutput('Network error: ' + error.toString());
      });
  };

  return (
    <div>
      updated
      <button onClick={runPythonScript}>Run Python Script</button>
      <pre>{output}</pre>
    </div>
  );
}

export default ChatBot;
