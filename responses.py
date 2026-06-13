import responses
import datetime 

print("=========AI Chatbot=========")
print("Welcome to the AI Chatbot!")
print("You can ask me anything, and I'll do my best to help you.")


responses = { 
    "hello" : "Hi there! How can I assist you today?",
    "how are you" : "I'm just a chatbot, but I'm doing great! Thanks for asking.",
    "what is your name" : "I'm an AI Chatbot created to assist you.",
    "thanks" : "You're welcome! If you have any more questions, feel free to ask.",
    "time" : f"The current time is {datetime.datetime.now().time()}.",
    "date" : f"Today's date is {datetime.datetime.now().date()}.",
    "joke" : "Why do programmers love Python? Because it's easy!",
    "who are you" : "I am Vishu's AI Assistant.",
    "bye" : "Goodbye! Have a great day!"
}


