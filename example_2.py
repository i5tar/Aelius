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
