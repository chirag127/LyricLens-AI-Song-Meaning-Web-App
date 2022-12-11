# from revChatGPT.revChatGPT import Chatbot
from pychatgpt import Chat
import os
import openai
import time


config = {"email": "whyiswhen@gmail.com", "password": "x$Mt5T@5yRg8nW2"}



def get_chat_response(prompt="Hello world"):

    # chatbot = Chatbot(config, conversation_id=None)

    # answer = chatbot.get_chat_response("Hello world", output="text")

    chat = Chat(email=config["email"], password=config["password"])

    answer, _, _ = chat.ask(prompt)

    return answer


openai.api_key = "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"


def codex_reply(message, song_name, artist):

    start = time.perf_counter()

    response = openai.Completion.create(
        model="code-davinci-002",
        prompt="",
        temperature=0.4,
        max_tokens=1717,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["###"],
    )

    end = time.perf_counter()

    print(f"Time taken: {end - start}")

    answer = response.choices[0].text

    answer = (
        f"1. The summary of the song {song_name} by {artist} is as follows:{answer}"
    )

    return answer


if __name__ == "__main__":

    prompt = "Hello world"

    response = get_chat_response(prompt)

    print(response)
