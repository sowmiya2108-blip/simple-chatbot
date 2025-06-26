def chatbot():
    print("Hello! I'm ChatBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if 'hello' in user_input or 'hi' in user_input:
            print("Bot: Hello there! How can I help you today?")
        elif 'how are you' in user_input:
            print("Bot: I'm just a bot, but I'm doing fine. Thanks for asking!")
        elif 'your name' in user_input:
            print("Bot: I'm a simple chatbot created by Python!")
        elif 'help' in user_input:
            print("Bot: I can help with simple questions. Try asking about my name or how I'm doing.")
        elif 'bye' in user_input:
            print("Bot: Goodbye! Have a great day!")
            break
        else:
            print("Bot: I'm not sure how to respond to that. Try asking something else.")

# Run the chatbot
chatbot()
