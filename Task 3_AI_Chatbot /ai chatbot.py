# AI CHATBOT

print("=== SIMPLE AI CHATBOT ===")
print("Type 'bye' to exit\n")

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! How are you?")

    elif user == "how are you":
        print("Bot: I am doing great!")

    elif user == "your name":
        print("Bot: My name is CodeAlpha Bot.")

    elif user == "what are you doing":
        print("Bot: I am chatting with you.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")
