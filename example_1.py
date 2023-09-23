import requests

def send_message(user_input):
    url = 'https://aelius.live/api/v1/chat'
    headers = {'Content-Type': 'application/json'}
    data = {'user_input': user_input}
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()
        display_message('Assistant', response_data['response'])
    except Exception as e:
        print(f"Error fetching AI response: {e}")

def display_message(who, message):
    # Implement this function based on how you want to display the message
    print(f"{who}: {message}")

# Example usage:
user_input_value = input("Type a message: ")
send_message(user_input_value)
