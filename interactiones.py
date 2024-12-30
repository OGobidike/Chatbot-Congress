from chatbot import Chatbotz

def chatbot_interaction(chatbots: Chatbotz, initial_message: str, turns: int = 5):
    message = initial_message
    for i in range(turns):
        for chatbot in chatbots:
            print(f"{chatbot.name}: {message}")
            message = chatbot.generate_response(message)
