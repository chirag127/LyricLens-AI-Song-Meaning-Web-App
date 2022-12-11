import contextlib
import os
import re
import requests
import json
from bs4 import BeautifulSoup


from lyricsgenius.genius import Genius
genius = Genius("STCcxkgkFP2fdoLI24XZBGrM-6EWnxV8epXSxiBeg5Xf1uydB0Yb_a6WzKVuKTRg")





def get_artist(actual_artist_name):

    artist_name = actual_artist_name.replace(" ", "_").lower()

    # remove all non-alphanumeric characters
    artist_name = "".join([char for char in artist_name if char.isalnum() or char == "_"])


    if os.path.exists("response/" + artist_name):


        # get all files names in the directory
        files = os.listdir("response/" + artist_name)


        # remove the extension
        files = [file.split(".")[0] for file in files]

    else:
        files = []

    artist = genius.search_artist(actual_artist_name, max_songs=10,  include_features=False,song_titles_to_exclude=files)
    return artist


if __name__ == "__main__":

    artist = get_artist("Justin Bieber")



    for a in artist.songs:
        with contextlib.suppress(Exception):
            print(a.artist)
            print('prited artist')
            print(a)
            print("printed a")
            print(a.title)
            print("printed a.title")
            # print(a.lyrics)
            print("printed a.lyrics")
            print(a.album)
            print("printed a.album")
            print(a.year)
            print("printed a.year")
            print(a.track_number)
            print("printed a.track_number")
            print(a.media)
            print("printed a.media")
            print(a.lyrics_state)

            print("printed a.lyrics_state")