def return_prompt(lyrics, artist,song_name):
    prompt = f"""Lyrics for {song_name} by {artist}:
{lyrics}

give the explaination for the above song in detail line by line and try to also include a review of the song
"""
    return prompt
