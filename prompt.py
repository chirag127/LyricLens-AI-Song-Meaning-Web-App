import errno
import os


def return_prompt(lyrics, artist, song_name, small_song_name):
    prompt = f"""Provide a complete detailed comprehensive in-depth verse-by-verse explanation of the song {song_name} by {artist} with
a verse-by-verse breakdown of the lyrics?
After your explanation,Include a summary of the song.
Additionally, Provide a review or opinion of the song.
Also Include Linguistic analysis of song lyrics to detect and interpret emotions, social tendencies, and language style which helps analyze emotions and feelings that musical artists express in their songs.

The lyrics for the song are as follows:

{lyrics}"""

    filename = f"{small_song_name}.txt"

    full_path = os.path.join(artist, filename)
    full_path = os.path.join("prompt", full_path)

    if not os.path.exists("prompt"):
        try:
            os.makedirs("prompt")
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    if not os.path.exists(f"prompt/{artist}"):
        try:
            os.makedirs(f"prompt/{artist}")
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(prompt)

    return prompt


def codex_prompt(lyrics, artist, song_name):
    prompt = f"""Lyrics for {song_name} by {artist} are as follows:


{lyrics}

Now, write a detailed explanation of the song {song_name} by {artist} with a verse-by-verse breakdown of the lyrics.

# your response:

1. The brief summary of the song {song_name} by {artist} is as follows:
"""

    with open("prompt.txt", "w", encoding="utf-8") as f:
        f.write(prompt)

    return prompt
