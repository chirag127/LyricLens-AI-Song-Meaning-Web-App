from cgpt import get_chat_response
from prompt import return_prompt
from azlyrics import get_lyrics

import os
from time import sleep


def get_lyrics_explaination_and_lyrics(url):
    delay = 1

    try:

        song_name = url.split("/")[-1].split(".")[0]

        file_name = song_name + ".txt"

        artist_name = url.split("/")[-2]

        full_path = os.path.join(artist_name, file_name)

        full_path = os.path.join("response", full_path)

        file_name = full_path

        # create directory if not exists
        if not os.path.exists("response"):
            os.mkdir("response")

        # create artist directory in response if not exists in response folder
        if not os.path.exists("response/" + artist_name):
            os.mkdir("response/" + artist_name)

        if os.path.exists(file_name):
            print("Response already exists for : " + song_name)

            delay = 0
            lyrics,song_name = get_lyrics(url)

            return open(file_name, "r", encoding="utf-8").read(),lyrics,song_name

        lyrics,song_name = get_lyrics(url)
        if artist_name == "charlieputh":


            artist_name = "Charlie Puth"

        elif artist_name == "ladygaga":

            artist_name = "Lady Gaga"

        elif artist_name == "justinbieber":

            artist_name = "Justin Bieber"

        elif artist_name == "taylorswift":

            artist_name = "Taylor Swift"

        elif artist_name == "edshereen":

            artist_name = "Ed Sheeran"

        elif artist_name == "arianagrande":

            artist_name = "Ariana Grande"

        elif artist_name == "shawnmendes":

            artist_name = "Shawn Mendes"

        elif artist_name == "billieeilish":

            artist_name = "Billie Eilish"

        elif artist_name == "postmalone":

            artist_name = "Post Malone"

        elif artist_name == "lilnasx":

            artist_name = "Lil Nas X"

        elif artist_name == "drake":

            artist_name = "Drake"

        elif artist_name == "kanyewest":

            artist_name = "Kanye West"

        elif artist_name == "paramore":

            artist_name = "Paramore"

        elif artist_name == "jungkook":

            artist_name = "Jungkook"

        elif artist_name == "metallica":

            artist_name = "Metallica"

        elif artist_name == "itzy":

            artist_name = "Itzy"

        elif artist_name == "skillet":

            artist_name = "Skillet"

        elif artist_name == "jamesarthur":

            artist_name = "James Arthur"

        elif artist_name == "lewiscapaldi":

            artist_name = "Lewis Capaldi"


        elif artist_name == "jellyroll":

            artist_name = "Jelly Roll"

        elif artist_name == "steelpanther":

            artist_name = "Steel Panther"

        elif artist_name == "jessiemurph":

            artist_name = "Jessie Murph"


        else:
            artist_name = artist_name.capitalize()


        prompt = return_prompt(lyrics, artist_name, song_name)

        response = get_chat_response(prompt)

        with open(file_name, "w", encoding="utf-8") as file:

            file.write(response)

        print("Response successfully written to file for : " + song_name)

        return response,lyrics,song_name

    except Exception as error:
        print("Error occured while fetching response for : " + song_name)
        print(error)
        print("Response not found for : " + song_name)

    finally:

        sleep(delay)


if __name__ == "__main__":

    with open("azlyrics_links.txt", "r", encoding="utf-8") as file:
        links = file.readlines()
    urls = [link.strip() for link in links]


    for url in urls:
        get_lyrics_explaination_and_lyrics(url)
