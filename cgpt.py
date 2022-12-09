# from revChatGPT.revChatGPT import Chatbot
from pychatgpt import Chat


config = {"email": "whyiswhen@gmail.com", "password": "x$Mt5T@5yRg8nW2"}

# chatbot = Chatbot(config, conversation_id=None)

chat = Chat(email=config["email"], password=config["password"])

def get_chat_response(prompt="Hello world"):

    # message = chatbot.get_chat_response(prompt)["message"]

    # return message

# Initializing the chat class will automatically log you in, check access_tokens
    answer = chat.ask(prompt)

    return answer

if __name__ == "__main__":

    prompt = "Hello world"

    response = get_chat_response(prompt)

    print(response)