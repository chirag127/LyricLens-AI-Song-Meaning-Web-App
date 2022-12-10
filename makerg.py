from cgpt import get_chat_response, codex_reply
from prompt import return_prompt, codex_prompt
from genius_api import get_artist

import os
from time import sleep




def get_lyrics_explaination_and_lyrics(song, codex=False):
    delay = 4

    try:

        actual_artist_name = song.artist

        actual_song_name = song.title

        song_name = actual_song_name.replace(" ", "_").lower()

        file_name = song_name + ".txt"

        artist_name = actual_artist_name.replace(" ", "_").lower()

        answer_full_path = os.path.join(artist_name, file_name)

        answer_full_path = os.path.join("response", answer_full_path)

        lyrics_full_path = os.path.join(artist_name, file_name)

        lyrics_full_path = os.path.join("lyrics", lyrics_full_path)

        if os.path.exists(answer_full_path):
            print("Response already exists for : " + song_name)

            return

        if not exists(
            "response/" + artist_name
        ):
            os.mkdir("response/" + artist_name)



        if codex:
            prompt = codex_prompt(song_name, artist_name, lyrics)

            response = codex_reply(prompt, song_name, artist_name)

        else:

            prompt = return_prompt(lyrics, actual_artist_name, actual_song_name,song_name)

            response = get_chat_response(prompt)

        if "large language model" in response:
            raise

        if "I don't know" in response:
            raise

        if "I don't understand" in response:

            raise


        with open(answer_full_path, "w", encoding="utf-8") as f:
            f.write(response)


        return response, lyrics, song_name

    except Exception as error:
        print("Error occured while fetching response for : " + song_name)
        print(error)
        print("Response not found for : " + song_name)

    finally:

        sleep(delay)


if __name__ == "__main__":

    # with open("azlyrics_links.txt", "r", encoding="utf-8") as file:
    #     links = file.readlines()
    # urls = [link.strip() for link in links]

    # for url in urls:
    #     get_lyrics_explaination_and_lyrics(url)

    popular_artists = [
        "Justin Bieber",
        "Charlie Puth",
        "Ed Sheeran",
        "Ariana Grande",
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
        "Marshmello",
        "BTS",
        "Maroon 5",
        "Lady Gaga",
        "Dua Lipa",
        "The Chainsmokers",
        "Logic",
        "Bruno Mars",
        "Lizzo",
        "Lil Dicky"]

    for artist in popular_artists:
        artist = get_artist(artist)

        for song in artist.songs:

            get_lyrics_explaination_and_lyrics(song)
