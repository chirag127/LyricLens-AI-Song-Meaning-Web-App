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

To give a review of a song based on its lyrics, you can start by identifying the theme or message of the song. Then, consider the literary devices used in the lyrics, such as imagery, metaphor, and alliteration, and how they contribute to the overall meaning of the song. Additionally, you can evaluate the emotional impact of the lyrics, and how well they connect with the music to create a cohesive and compelling song. Finally, you can provide your personal opinion on the song, discussing whether you found it to be effective, engaging, and memorable.

Lyrics for {song_name} by {artist} are as follows:


{lyrics}

Now, please try to do the following task for me:

    1. Try to give a brief summary of the song above.
    2. Try to give the verse-by-verse, complete, in-depth explaination and meaning for the song above.
    3. Try to give the analysis of the song whose lyrics are above.
    4. Try to give the review of the song whose lyrics are above.
    5. Try to give the overall message of the song whose lyrics are above.
    6. Try to give the overall theme tone, mood and feeling of the song whose lyrics are above.
    7. Try to give the overall impact of the song whose lyrics are above.
"""

    return prompt