import contextlib


from lyricsgenius.genius import Genius
genius = Genius("STCcxkgkFP2fdoLI24XZBGrM-6EWnxV8epXSxiBeg5Xf1uydB0Yb_a6WzKVuKTRg")





def get_artist(artist_name):
    artist = genius.search_artist(artist_name, max_songs=5,  include_features=True)
    return artist


if __name__ == "__main__":

    artist = get_artist("C2C")



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