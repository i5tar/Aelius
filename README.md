# Aelius API

## Introduction
Welcome to the Aelius API tutorial. This guide will help you integrate the free and open Aelius chatbot into your website.

## Getting Started
The Aelius API is open and free for everyone. No account registration is required. Simply follow this guide to start integrating the chatbot into your platform.

## Setting Up the Chat UI
Use the provided HTML structure from the example to create a chat interface. This includes a chat container, input box, and send button.

### HTML
```html
<div id="chatContainer">
    <h1>Welcome to Aelius AI</h1>
    <div id="chatBox" style="display: flex; flex-direction: column; opacity: 0;"></div>
</div>
<div id="inputContainer">
    <input type="text" id="userInput" placeholder="Type a message...">
    <button onclick="sendMessage()">Send</button>
</div>
```

## Connecting to the API
Use the fetch API or another HTTP client to send a POST request to 'https://aelius.live/api/v1/chat'. The body of the request should contain the user's message.

### JavaScript
```javascript
async function sendMessage() {
    const message = userInput.value;
    try {
        const response = await fetch('https://aelius.live/api/v1/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_input: message })
        });
        const responseData = await response.json();
        displayMessage('Assistant', responseData.response);
    } catch (error) {
        console.error("Error fetching AI response:", error);
    }
}
```
