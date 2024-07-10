import random

# Define some responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks!", "Doing well, thank you!", "Pretty good!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "default": ["Sorry, I didn't understand that.", "I'm not sure what you mean."],
}

# Function to get a response to a user input
def get_response(message):
    # Convert the message to lowercase
    message = message.lower()
    
    # Check if the message is in our responses dictionary
    if message in responses:
        return random.choice(responses[message])
    else:
        return random.choice(responses["default"])

# Main loop
while True:
    # Get user input
    user_input = input("You: ")
    
    # Check if the user wants to exit
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    
    # Get and print the chatbot's response
    response = get_response(user_input)
    print("Chatbot:", response)
