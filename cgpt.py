# from pychatgpt import Chat
import time

import openai
from revChatGPT.Official import Chatbot

config = {"email": "whyiswhen@gmail.com", "password": "x$Mt5T@5yRg8nW2"}
# config = {
#   "session_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..2wVur5Ri0liyrQg2.qGw5BTRDktYQpjJdeq09cW4JZQA7sLFzPzsbrYahzRCGKHW7kRJcLIDNgIeqLO5PZyN93n2_FOVTR3cbgTtbvE2z4xW648nDtVtbcmWgJ2TBjS8EluvVk2_t0E-Kwtian1OJaWz0J9rDV5z6eNzMv_XfCFZwReiJGbqENDSkoXkkNqiFNPLVTFhx99QfQiEahvGlq2H9OgfW31uac95lceFL5YwFJrxTS3s2sXUuE_sTykyFPFRfb7AXWCWA3mWHyQJQcBuiIQd0dM3QPGKISoNrxxV9iDdKDZLacmtmtUxC-myuvwLZqxIoGq53ZXlLj1LFMiCZrTJ14r5cXmKzpODvLH7u5FomK2i2DIXt3_cv4Oze-zw0ZguqBJ8DjYipzC4NSXuPXi8sEKygVJJt8q2istCBsJAKZgYlkmVsIm_IZ6yGNMOqeaEskkywSgKcmitaxjFy7E40_aVkc4ZCy5kd353oRAb9irY1Z8yFdhRBuvdeeOhiaHvl4rILvdghzGufSrelaRjC17777Q1G1n8BR2N1qOwdoDMLxZhWPDKlvcHcubcsyqio7zitLBazPYxL4HzvrR9qEQyuP5oepjyDYUDZuI8ZaI1wO6xDBlul_Aa8qlx3MgyMF3pTP9gfS0GfB2dqS9RDnABk8yx4p4nEy3rce5rTVu8GRFV13oj69Pzqt8rMAXZuu_YUc1CTv_quHHhExw9qAV-Hg42QsvbzNu6v8UVxV3_Dp-7eX8qBWbnuVeSPe_dmYwHTS4os8sl-ZrhUT0jCZOnnWsW42-aIiqPqfvN-J8EvYfgobFC-MdT8UX1OgIn9jnSg0m3csjGbvLRD28LY9RLVzL1VoHcI96wz9GlZj2FhQKYsQJAJMYTfQgNvcdsMZVp-nqlOkUvG9rQtxPALbzoOs6zvPFIDOH4Axgij3L8bPgGZqr26-MJo4cmATyJ5gDXnfC3wzH-WZ8N9i_8SKfzbSJYjDD2QAh50qePP2Esat53r9ZX6EcixKhkta-CgaZeFkTw0qK2X7zC81rOqxXyiKOtlEwkVUGz5rLwlWtmLyN3zXQwT_EpXdsjmH-1UMCHSq-yOx3CVzW0nnfpE5dTt50AtN-IZDNxElpdEvaZ5idVZTpLDVagzLKnrtEYW9irMIcBI7tqq6txTsX7CRecYFvvL2nN2TGgdCDbfMgO-c2GuHdwCB0ClrP8kysaCySgd98FhgrJibTVmIgYVZ9XEoXPMm0k0XIQQ3tX1kB9J-Pf-5sdtaZrD5VlhynjU_4Hi4vX8S3ayDWCaYW1uxf0pvhR52GLs583nYLCrHT2a7OLxi4HUy3eNEM6f5S6YXZbc5tLfPs-MyAxBKN1Ek28hl2vyvmwL_NZUABj6n3LoAOFH49ujU-44eCuF5sO2q6aUQ-cqZba9gBfHPXrO9nFHT8Z_FjH2FtdU6UhENsXGJzlhGZA_xBV0-tV1jDPtBHyImz6Bnk0iizyTwJpue0hwemqF_je6by1djUMRhkILWFOzcoXsYWSIvuBgfoBY5EmxWjQeXqEbuvCdRLrKdMce9Ct6V1MSRcZTvAht12_867RDU12s3M25fSQ0KNQEnEFo2JTKuaoMQlYAXZMx2E6bS2RbyO7yJaw9WMk0-V0idWgylZwEUwBBgtLl7q8emmPsLVbwG9PyzsEf5t-psSwD8t0m4rjeKeLgx3QgZSUtUWGDPYjnTFv1e77tlE6kWq1l2co-umaCe0K8-5Vuhjf5besQsvllU6sWEJhZW_HGn2lo6BShUqfr_qDoYb6BuKkEMOD0ip5GkbA_h8lR02PsHht7a0zUksAf7h6_3WLxY3Ht9pku8C5LETJcbG0ZYxS1NY05TYbeZnwddPqfk9e25HzgQ_XgxD0dJ7MttZov2MncCgpaTftRYTafbCtQXe6bz7L5XZCpZDYi7umtAR_hGUiM5933a05FoE1w9s03gPhf0se6a1IDBYqK0jCKwiiFSJbof-PQQdgjx6eH08s0YrVC_NkzjkRjhrX4HBMVzgaBhshA1al6oJoBOofgc1oknwio_Jly29AiJOPbkYm2exlFSx7krBLa7pkrpRGc7Q3Ql8hXIBufuKqRgJotcA9OlOsqNHh_oDYHvPvrHA8UiJPjdnDmHYeDwKCX1QjzV4lUZpwtIIBMWuMXCGFoDton67ctgiBSV2wGRykOAukUsbrtjcyM18Iqc1wZ3w2wSkdvJ7bZwE0ru2JcvQsRhvMFJXDkDj1XaD_qpXGbzHKcmqlzTNQ9jnciZqZOEH1Cr_ID0nfs4gCYcfcqXDCekT-P8yxthxUXiC7-ydMxiHxSUrRZVM_KU5uAzwqAOYJg5TKJgz5b4JFSroJumZkh.Inb6h5mppeGjmYb4piGGmA",
#   "cf_clearance": "8m4g2OYfVwWnYe.R0g.KWFOzWeWSCbckSIokKjwZ8S8-1670839392-0-160",
#   "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"
# }


def get_chat_response(prompt="Hello world"):
    chatbot = Chatbot(config=config, conversation_id=None)

    answer = chatbot.get_chat_response("Hello world", output="text")

    # chat = Chat(email=config["email"], password=config["password"])

    # answer, _, _ = chat.ask(prompt)

    print(answer)

    answer = answer["message"]

    return answer


openai.api_key = "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"


def codex_reply(message, song_name, artist):

    start = time.perf_counter()

    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=message,
        temperature=0.3,
        max_tokens=1717,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["###"],
    )

    end = time.perf_counter()

    print(f"Time taken: {end - start}")

    answer = response.choices[0].text

    a = f"1. The summary of the song {song_name} by {artist} is as follows:{answer}"

    print(a)

    return a


if __name__ == "__main__":

    prompt = "Hello"

    response = get_chat_response(prompt)

    print(response)

    prompt = "how to make a chatbot"

    response = get_chat_response(prompt)

    print(response)

    prompt = "how to make a chatbot"

    response = get_chat_response(prompt)

    print(response)
