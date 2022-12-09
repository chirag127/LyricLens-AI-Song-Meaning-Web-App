def return_prompt(lyrics, artist,song_name):
    prompt = f"""Lyrics for {song_name} by {artist} are as follows:


{lyrics}

Try to tell me a verse-by-verse explanation of the song {song_name} by {artist} whose lyrics are given above in detail.
please also try to give a overall summary and review of the song {song_name} by {artist}."""




    with open("prompt.txt", "w", encoding="utf-8") as f:
        f.write(prompt)

    return prompt

def codex_prompt(lyrics, artist,song_name):
    prompt = f"""I am try to make a blog which contains the analysis, review, explanation etc of the song {song_name} by {artist}.

Lyrics for {song_name} by {artist} are as follows:


{lyrics}

Now, please try to do the following task for me:

    1. You may try to give a brief summary of the song {song_name} by {artist}.
    2. You may try to give the verse-by-verse, complete, in-depth explaination and meaning for the song {song_name} by {artist} whose lyrics are given above. Other details for this are:

        A. You may try to explain the meaning of the first verse, second verse, third verse, etc. of the song {song_name} by {artist} whose lyrics are given above. for example, you can say that the first verse of the song is about the following things: ((first verse explaination)).
        B. You may try to also explain the meaning of the chorus, bridge, etc. of the song {song_name} by {artist} whose lyrics are given above. for example, you can say that the chorus of the song is about the following things: ((chorus explaination)).
        C. You may try to explain the chorus only once of the song {song_name} by {artist} whose lyrics are given above.. You don't need to explain the chorus again and again in the explaination of the verses. For example, if you have already explained the chorus in the explaination of the ffirst verse, then you don't need to explain the chorus again in the explaination of the second verse, third verse, etc.
        D. This task is very important for me. Please try to do this task for me. I will be very thankful to you if you do this task for me.

    3. You may try to give the complete analysis of the song {song_name} by {artist} whose lyrics are given above.
    4. You may try to give the complete mood of the song {song_name} by {artist} whose lyrics are given above.
    5. You may try to give the complete genre of the song {song_name} by {artist} whose lyrics are given above.
    6. You may try to give the complete theme of the song {song_name} by {artist} whose lyrics are given above.
    7. You may try to give the complete message of the song {song_name} by {artist} whose lyrics are given above.
    8. You may try to give the complete story of the song {song_name} by {artist} whose lyrics are given above.
    9. You may try to give the complete meaning of the song {song_name} by {artist} whose lyrics are given above.
    10. You may try to give the complete review of the song {song_name} by {artist} whose lyrics are given above.
    11. enter ### to stop the generation.

# your response:

1. The brief summary of the song {song_name} by {artist} is as follows:
"""



    with open("prompt.txt", "w", encoding="utf-8") as f:
        f.write(prompt)



    return prompt
