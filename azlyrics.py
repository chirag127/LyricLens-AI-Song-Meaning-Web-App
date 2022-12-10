"""
This script is used to fetch lyrics from azlyrics.com"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep
import os


def get_lyrics(url="https://www.azlyrics.com/lyrics/charlieputh/themoment.html"):
    delay = 14
    seperator = "==="
    try:
        song_name = url.split("/")[-1].split(".")[0]

        file_name = song_name + ".txt"

        artist_name = url.split("/")[-2]

        full_path = os.path.join(artist_name, file_name)

        full_path = os.path.join("lyrics", full_path)

        file_name = full_path

        # create directory if not exists
        if not os.path.exists("lyrics"):
            os.mkdir("lyrics")

        # create artist directory in lyrics if not exists in lyrics folder
        if not os.path.exists("lyrics/" + artist_name):
            os.mkdir("lyrics/" + artist_name)

        if os.path.exists(file_name):
            print("Lyrics already exists for : " + song_name)

            actual_song_name_and_lyrics = open(file_name, "r", encoding="utf-8").read()

            delay = 0
            actual_song_name = actual_song_name_and_lyrics.split(seperator)[0]

            lyrics = actual_song_name_and_lyrics.split(seperator)[1]

            return lyrics, actual_song_name

        html_page = urlopen(url)
        soup = BeautifulSoup(html_page, "html.parser")

        html_pointer = soup.find("div", attrs={"class": "ringtone"})
        actual_song_name = html_pointer.find_next("b").contents[0].strip()
        lyrics = html_pointer.find_next("div").text.strip()

        with open(file_name, "w", encoding="utf-8") as file:

            file.write(actual_song_name + seperator + lyrics)

        print("Lyrics successfully written to file for : " + song_name)

        return lyrics, actual_song_name

    except Exception as e:
        print("Error occured while fetching lyrics for : " + song_name)
        print(e)
        print("Lyrics not found for : " + song_name)

    finally:
        sleep(delay)


if __name__ == "__main__":

    with open("azlyrics_links.txt", "r", encoding="utf-8") as file:
        links = file.readlines()
    urls = [link.strip() for link in links]

    for url in urls:
        try:
            lyrics = get_lyrics(url)
        except Exception as e:
            print(e)
