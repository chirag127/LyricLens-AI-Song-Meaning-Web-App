"""OpenAI lyrics/meaning generator — set OPENAI_API_KEY env var."""

import os

import openai

openai.api_key = os.environ["OPENAI_API_KEY"]


def get_meaning(song_name, artist, lyrics=""):
    prompt = f"Explain the meaning of the song '{song_name}' by {artist}."
    if lyrics:
        prompt += f"\n\nLyrics:\n{lyrics[:3000]}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1024,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    song = os.environ.get("SONG", "Bohemian Rhapsody")
    artist = os.environ.get("ARTIST", "Queen")
    print(get_meaning(song, artist))
