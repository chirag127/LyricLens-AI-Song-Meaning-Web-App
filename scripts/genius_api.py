"""Genius lyrics scraper — set GENIUS_TOKEN env var before running."""

import contextlib
import os

from lyricsgenius.genius import Genius

genius = Genius(os.environ["GENIUS_TOKEN"])


def get_artist(actual_artist_name, max_songs=10):
    artist_name = actual_artist_name.replace(" ", "_").lower()
    artist_name = "".join(c for c in artist_name if c.isalnum() or c == "_")

    files = []
    output_dir = os.path.join("response", artist_name)
    if os.path.exists(output_dir):
        files = [f.split(".")[0] for f in os.listdir(output_dir)]

    return genius.search_artist(
        actual_artist_name,
        max_songs=max_songs,
        include_features=False,
        song_titles_to_exclude=files,
    )


if __name__ == "__main__":
    artist_name = os.environ.get("ARTIST", "Taylor Swift")
    artist = get_artist(artist_name)
    for song in artist.songs:
        with contextlib.suppress(Exception):
            print(song.title, "|", song.artist)
