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

## Displaying the Response
Once you receive a response from the API, display it in the chat container. Ensure you handle any errors or exceptions that might occur.

### JavaScript
```javascript
function displayMessage(who, message) {
    const messageDiv = document.createElement('p');
    if (who === 'You') {
        messageDiv.classList.add('user');
    }
    messageDiv.innerHTML = `<strong>${who}:</strong> ${message}`;
    chatBox.appendChild(messageDiv);
}
          
```

## Example
A simple API usage example written in Python. More examples can be found in this repository.

### Python
```python
import requests

def send_message_to_aelius(user_input):
    url = 'https://aelius.live/api/v1/chat'
    headers = {'Content-Type': 'application/json'}
    data = {'user_input': user_input}
    
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()['response']
    except Exception as e:
        print(f"Error fetching AI response: {e}")
        return None

def main():
    print("Welcome to the Aelius Command-Line Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting chatbot. Goodbye!")
            break
        response = send_message_to_aelius(user_input)
        if response:
            print(f"Assistant: {response}")

main()
```

## API Guidelines
Avoid straining the API, we don't have unlimited computing power and if you wish for Aelius to remain free and open then please use the API within reason.

## Enhancements & Best Practices
You can enhance the chatbot by adding features like predefined prompts, error handling, and more. Here are some best practices to consider:

* Always handle API errors gracefully.
* Consider adding a loading animation while waiting for the API response.
* Regularly test the chatbot to ensure it's functioning correctly.
* Avoid straining the API.
