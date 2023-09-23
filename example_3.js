const express = require('express');
const fetch = require('node-fetch');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.post('/send_message', async (req, res) => {
    const userInput = req.body.user_input;
    const response = await sendMessageToAelius(userInput);
    res.json({ response: response });
});

async function sendMessageToAelius(userInput) {
    const url = 'https://aelius.live/api/v1/chat';
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_input: userInput })
    });
    const data = await response.json();
    return data.response;
}

app.listen(3000, () => {
    console.log('Server started on http://localhost:3000');
});
