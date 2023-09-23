from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.json['user_input']
    response = send_message_to_aelius(user_input)
    return jsonify({'response': response})

def send_message_to_aelius(user_input):
    url = 'https://aelius.live/api/v1/chat'
    headers = {'Content-Type': 'application/json'}
    data = {'user_input': user_input}
    
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()['response']
    except Exception as e:
        print(f"Error fetching AI response: {e}")
        return "Sorry, I couldn't process that request."

if __name__ == '__main__':
    app.run(debug=True)
