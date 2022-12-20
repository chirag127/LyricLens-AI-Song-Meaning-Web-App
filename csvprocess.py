from orchard import get_orchard_response


import os
from time import sleep
from makerg import line_21
from prompt import return_prompt


def get_lyrics_explaination_and_lyrics_csv(artist, title, album, date, year, lyric):
    delay = 30

    try:

        actual_artist_name = artist

        actual_song_name = title

        song_name, file_name, artist_name, answer_full_path = line_21(actual_artist_name, actual_song_name)

        if os.path.exists(answer_full_path):
            print(f"Response already exists for : {song_name}")

            return

        lyrics_full_path = os.path.join(artist_name, file_name)

        lyrics_full_path = os.path.join("lyrics", lyrics_full_path)

        if not os.path.exists(f"response/{artist_name}"):
            os.mkdir(f"response/{artist_name}")

        if not os.path.exists(f"lyrics/{artist_name}"):
            os.mkdir(f"lyrics/{artist_name}")



        lyrics = lyric


        # remove the first line of the lyrics

        # lyrics = lyrics.split("\n")[1:]

        # lyrics = "\n".join(lyrics)


        if not os.path.exists(lyrics_full_path):
            with open(lyrics_full_path, "w", encoding="utf-8") as file:
                file.write(lyrics)


        actual_song_name = title


        prompt = return_prompt(lyrics, actual_artist_name, actual_song_name,song_name)


        print(f"getting response for : {song_name}")

        response = get_orchard_response(prompt)

        print(f"got response for : {song_name}")

        sleep(delay)

        if "large language model" in response:
            raise

        if "I don't know" in response:
            raise

        if "I don't understand" in response:

            raise

        if "You've made too many requests!" in response:

            print("You've made too many requests!")
            raise


        with open(answer_full_path, "w", encoding="utf-8") as f:
            f.write(response)

        print(f"Response saved for : {song_name}")

        return response, lyrics, song_name

    except Exception as error:
        print(f"Error occured while fetching response for : {song_name}")
        print(error)
        print(f"Response not found for : {song_name}")

def main():
    import csv
    import os
    songs = []


    def process_song(song):
        artist = song[0]
        title = song[1]
        album = song[2]
        date = song[3]
        year = song[4]
        lyric = song[5]

        get_lyrics_explaination_and_lyrics_csv(artist, title, album, date, year, lyric)

    for filename in os.listdir("csv"):

        if filename == "ArianaGrande.csv":
            if filename.endswith(".csv"):
                print("Processing " + filename)
                with open("csv/" + filename, "r") as f:
                    reader = csv.reader(f)

                    # skip header
                    next(reader)

                    # header was Artist,Title,Album,Date,Lyric,Year
                    # we want Artist,Title,Album,Date,Year,Lyric
                    songs = []

                    for row in reader:
                        artist = row[0]
                        title = row[1]
                        album = row[2]
                        date = row[3]
                        year = row[5]
                        lyric = row[4]

                        songs.append([artist, title, album, date, year, lyric])

            else:
                continue
        else:
            if filename.endswith(".csv"):
                print("Processing " + filename)
                with open("csv/" + filename, "r") as f:
                    reader = csv.reader(f)

                    # skip header
                    next(reader)

                    # header was ,Artist,Title,Album,Year,Date,Lyric
                    # we want Artist,Title,Album,Date,Year,Lyric

                    for row in reader:
                        artist = row[1]
                        title = row[2]
                        album = row[3]
                        date = row[5]
                        year = row[4]
                        lyric = row[6]

                        songs.append([artist, title, album, date, year, lyric])

            else:
                continue


    for song in songs:
        process_song(song)


if __name__ == "__main__":
    main()