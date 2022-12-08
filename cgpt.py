from revChatGPT.revChatGPT import Chatbot

config = {"email": "whyiswhen@gmail.com", "password": "x$Mt5T@5yRg8nW2"}

chatbot = Chatbot(config, conversation_id=None)


def get_chat_response(prompt="Hello world"):

    message = chatbot.get_chat_response(prompt)["message"]

    return message
