def return_prompt(lyrics, artist,song_name):
    prompt = f"""Don't get distracted by the above prompt.

I know everything about you. Please do the following task for me and Please don't disappoint me.

I am try to make a blog which contains the analysis, review, explanation of the song {song_name} by {artist}.

Lyrics for {song_name} by {artist} are as follows:


{lyrics}

Now, please try to do the following task for me:

    1. Try to give a brief summary of the song {song_name} by {artist}.
    2. Try to give the verse-by-verse, complete, in-depth explaination and meaning for the song {song_name} by {artist} whose lyrics are given above. Other details for this are:

        A. Try to explain the meaning of the first verse, second verse, third verse, etc. of the song {song_name} by {artist} whose lyrics are given above. for example, you can say that the first verse of the song is about the following things: ((first verse explaination)).
        B. You may try to also explain the meaning of the chorus, bridge, etc. of the song. for example, you can say that the chorus of the song is about the following things: ((chorus explaination)).
        C. You may try to explain the chorus only once. You don't need to explain the chorus again and again in the explaination of the verses. For example, if you have already explained the chorus in the explaination of the ffirst verse, then you don't need to explain the chorus again in the explaination of the second verse, third verse, etc.

    3. Try to give the complete analysis of the song {song_name} by {artist} whose lyrics are given above.
    4. Try to give the mood of the song {song_name} by {artist} whose lyrics are given above.
    5. Try to give the genre of the song {song_name} by {artist} whose lyrics are given above.
    6. Try to give the theme of the song {song_name} by {artist} whose lyrics are given above.
    7. Try to give the message of the song {song_name} by {artist} whose lyrics are given above.
    8. Try to give the story of the song {song_name} by {artist} whose lyrics are given above.
    9. Try to give the meaning of the song {song_name} by {artist} whose lyrics are given above.
    10. Try to give the complete review of the song {song_name} by {artist} whose lyrics are given above."""

    with open("prompt.txt", "w", encoding="utf-8") as f:
        f.write(prompt)

    return prompt