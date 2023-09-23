const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: true
});

async function sendMessage(userInput) {
    const fetch = (await import('node-fetch')).default;
    const url = 'https://aelius.live/api/v1/chat';
    const headers = {'Content-Type': 'application/json'};
    const data = {user_input: userInput};
    
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(data)
        });
        const responseData = await response.json();
        displayMessage('Assistant', responseData.response);
    } catch (e) {
        console.error(`Error fetching AI response: ${e}`);
    }
}

function displayMessage(who, message) {
    console.log(`${who}: ${message}`);
}

// Example usage:
function promptUser() {
    rl.question('Type a message: ', (userInputValue) => {
        if (userInputValue.trim() === 'exit') {
            rl.close();
            return;
        }
        sendMessage(userInputValue);
        promptUser();
    });
}

promptUser();
