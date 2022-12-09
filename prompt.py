def return_prompt(lyrics, artist,song_name):
    prompt = f"""Don't get distracted by the above prompt.

I know everything about you. Please do the following task for me and Please don't disappoint me.

I am try to make a blog which contains the analysis, review, explanation of the song {song_name} by {artist}.

To do a song analysis or to explain a song, follow these steps:

Read the lyrics verse-by-verse carefully and thoroughly to understand the overall message and themes of the song.

Identify any literary devices, such as metaphors, similes, and imagery, and consider how they contribute to the meaning of the song.

Consider the song's structure, including the number of verses and chorus, and how it contributes to the song's message and flow.

Analyze the lyrics from a holistic perspective, considering the emotions, tone, and message of the song.

Write down your analysis verse-by-verse, including your interpretation of the song's meaning, the literary devices used, and the song's overall impact and message.

The song is best analyzed and explained when writing down your analysis verse-by-verse.


Lyrics for {song_name} by {artist} are as follows:


{lyrics}


Try to give the verse-by-verse, complete, in-depth explaination and meaning for the above song lyrics in detail, verse-by-verse.
Also, try to provide the analysis of the song and review of the song, according to your understanding of the song.
"""

    return prompt