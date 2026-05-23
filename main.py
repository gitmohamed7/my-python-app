from chatbot import chat

print("Claude Chatbot - type 'quit' to exit")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = chat(user_input)
    print(f"Claude: {response}\n")