import React, { useState } from 'react';

function App() {
  const [helpText, setHelpText] = useState('Helpful notes will appear here');

  function setupHelp() {
    const helpText = [
      { id: "email", help: "Your e-mail address" },
      { id: "name", help: "Your full name" },
      { id: "age", help: "Your age (you must be over 16)" }
    ];

    return helpText.map(item => ({
      id: item.id,
      onFocus: () => setHelpText(item.help)
    }));
  }

  const inputs = setupHelp();

  return (
    <div style={{ padding: '20px' }}>
      <p>{helpText}</p>
      {inputs.map(item => (
        <p key={item.id}>
          {item.id}: <input 
            type="text" 
            id={item.id} 
            onFocus={item.onFocus}
          />
        </p>
      ))}
    </div>
  );
}

export default App;