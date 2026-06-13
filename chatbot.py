from responses import responses
from datetime import datetime

chat_history = []

print("=" * 50)
print("      DECODELABS AI CHATBOT")
print("=" * 50)
print("Type 'help' for commands")
print("Type 'exit' to quit")
print()


def chatbot_response(user_input):

    if user_input == "time":
        return datetime.now().strftime("%H:%M:%S")

    elif user_input == "date":
        return datetime.now().strftime("%d-%m-%Y")

    elif user_input == "joke":
        return "Why do programmers love Python? Because it's easy!"

    return responses.get(
        user_input,
        "Sorry, I don't understand."
    )


while True:

    user = input("You: ").lower().strip()

    if user == "exit":
        print("Bot: Goodbye!")
        break

    reply = chatbot_response(user)

    print("Bot:", reply)

    chat_history.append(
        f"You: {user}"
    )

    chat_history.append(
        f"Bot: {reply}"
    )


with open(
    "chat_history.txt",
    "w"
) as file:

    for message in chat_history:
        file.write(message + "\n")