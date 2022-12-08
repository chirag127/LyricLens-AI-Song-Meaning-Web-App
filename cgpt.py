from revChatGPT.revChatGPT import Chatbot

config ={
    "email": "whyiswhen@gmail.com",
    "password": "x$Mt5T@5yRg8nW2"
}

chatbot = Chatbot(config, conversation_id=None)

message = chatbot.get_chat_response("Hello world")['message']
print(message)



