import React, { useState, useEffect } from 'react';

function Closure() {
  const [helpText, setHelpText] = useState('Helpful notes will appear here');

  function showHelp(help) {
    console.log('Showing help:', help);
    setHelpText(help);
  }

  function setupHelp() {
    var helpText = [
      {'id': 'email', 'help': 'Your e-mail address'},
      {'id': 'name', 'help': 'Your full name'},
      {'id': 'age', 'help': 'Your age (you must be over 16)'}
    ];

    var handlers = [];
    
    for (var i = 0; i < helpText.length; i++) {
      var item = helpText[i];
      handlers.push({
        id: item.id,
        onFocus: () => {
          console.log('item.onFocus', item.id);
          showHelp(item.help);
        }
      });
    }
    console.log('All handlers created:', handlers);
    return handlers;
  }

  const inputs = setupHelp();

  return (
    <div style={{ padding: '20px' }}>
      <p id="help">{helpText}</p>
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

export default Closure;