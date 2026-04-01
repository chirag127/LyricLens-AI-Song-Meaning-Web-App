import os
import random
import time
from time import sleep

from revChatGPT.Official import Chatbot

from cgpt import codex_reply
from genius_api import get_artist
from prompt import codex_prompt, return_prompt

# a = random.randint(1, 1000)
# print("Sleeping for {} seconds".format(a))
# sleep(a)

# Initialize chatbot


def chat(i):

    PROMPT = i

    # with open(file_name, "w") as f:

    #     f.write(PROMPT + "\n")
    # print(PROMPT)
    # divide prompt by first space
    # PROMPT = PROMPT.split(" ", 1)[1]

    # PROMPT = "write in detail to explain the concept of " + PROMPT
    start = time.perf_counter()
    print("User: " + PROMPT)

    api_keys = [
        "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",
        "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",
        "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",
    ]

    chatbot = Chatbot(api_key=random.choice(api_keys))

    response = chatbot.ask(PROMPT)
    print("ChatGPT: " + response["choices"][0]["text"])
    end = time.perf_counter()

    print(f"Time taken: {end - start:0.4f} seconds")

    return response["choices"][0]["text"]


def line_21(actual_artist_name, actual_song_name):
    song_name = actual_song_name.replace(" ", "_").lower()

    song_name = "".join([char for char in song_name if char.isalnum() or char == "_"])

    file_name = f"{song_name}.txt"

    artist_name = actual_artist_name.replace(" ", "_").lower()

    artist_name = "".join(
        [char for char in artist_name if char.isalnum() or char == "_"]
    )

    answer_full_path = os.path.join(artist_name, file_name)

    answer_full_path = os.path.join("response", answer_full_path)
    return song_name, file_name, artist_name, answer_full_path


def get_lyrics_explaination_and_lyrics(song, codex=False):
    delay = 10

    try:

        actual_artist_name = song.artist

        actual_song_name = song.title
        song_name, file_name, artist_name, answer_full_path = line_21(
            actual_artist_name, actual_song_name
        )

        if os.path.exists(answer_full_path):
            print(f"Response already exists for : {song_name}")

            return

        lyrics_full_path = os.path.join(artist_name, file_name)

        lyrics_full_path = os.path.join("lyrics", lyrics_full_path)

        if not os.path.exists(f"response/{artist_name}"):
            os.mkdir(f"response/{artist_name}")

        if not os.path.exists(f"lyrics/{artist_name}"):
            os.mkdir(f"lyrics/{artist_name}")

        lyrics = song.lyrics

        # remove the first line of the lyrics

        lyrics = lyrics.split("\n")[1:]

        lyrics = "\n".join(lyrics)

        if not os.path.exists(lyrics_full_path):
            with open(lyrics_full_path, "w", encoding="utf-8") as file:
                file.write(lyrics)

        if codex:
            prompt = codex_prompt(song_name, artist_name, lyrics)

            response = codex_reply(prompt, song_name, artist_name)

        else:

            prompt = return_prompt(
                lyrics, actual_artist_name, actual_song_name, song_name
            )

            print(f"getting response for : {song_name}")

            response = chat(prompt)
            print(f"got response for : {song_name}")

        if "large language model" in response:
            raise

        if "I don't know" in response:
            raise

        if "I don't understand" in response:

            raise

        sleep(delay)

        with open(answer_full_path, "w", encoding="utf-8") as f:
            f.write(response)

        print(f"Response saved for : {song_name}")

        return response, lyrics, song_name

    except Exception as error:
        print(f"Error occured while fetching response for : {song_name}")
        print(error)
        print(f"Response not found for : {song_name}")


def main():

    # with open("azlyrics_links.txt", "r", encoding="utf-8") as file:
    #     links = file.readlines()
    # urls = [link.strip() for link in links]

    # for url in urls:
    #     get_lyrics_explaination_and_lyrics(url)

    popular_artists = [
        # "Justin Bieber",
        # "Charlie Puth",
        # "Ed Sheeran",
        # "Ariana Grande",
        "Shawn Mendes",
        "Billie Eilish",
        "Nicki Minaj",
        "Taylor Swift",
        "Drake",
        "Selena Gomez",
        "Cardi B",
        "Khalid",
        "Camila Cabello",
        "Halsey",
        "Imagine Dragons",
        "J Balvin",
        "J. Cole",
        "Jaden Smith",
        "Jason Derulo",
        "Jonas Brothers",
        "Justin Bieber",
        "Kanye West",
        "Katy Perry",
        "Kendrick Lamar",
        "Khalid",
        "Lady Gaga",
        "Lana Del Rey",
        "Lil Nas X",
        "Lil Wayne",
        "Lizzo",
        "Logic",
        "Maroon 5",
        "Marshmello",
        "BTS",
        "Maroon 5",
        "Lady Gaga",
        "Dua Lipa",
        "The Chainsmokers",
        "Logic",
        "Bruno Mars",
        "Lizzo",
        "Lil Dicky",
    ]

    for artist in popular_artists:

        try:
            artist = get_artist(artist)

            for song in artist.songs:

                get_lyrics_explaination_and_lyrics(song, True)

                sleep(10)
        except Exception as error:
            print(error)
            continue


if __name__ == "__main__":
    main()
