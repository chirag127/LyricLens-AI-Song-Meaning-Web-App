import random
import webbrowser
from time import sleep

import pyautogui
import pyperclip
from makerep import get_lyrics_explaination_and_lyrics


def return_article(lyrics, explaination, author="Chirag Singhal"):
    article = f"""The explanation is:

{explaination}




The lyrics are:


{lyrics}







This article was written by {author}"""

    return article


def return_title(song_name, artist="Charlie Puth"):

    title = random.choice(
        [
            f"Deconstructing the meaning behind {artist}'s hit single {song_name}",
            f"A closer look at the musical elements of {song_name} by {artist}",
            f"{artist}'s {song_name}: a lyrical and musical analysis",
            f"The hidden messages in {artist}'s {song_name}: an in-depth review",
            f"Unpacking the themes and symbolism in {song_name} by {artist}",
            f"Deconstructing the Lyrics of {song_name}: A Deep Dive into the Meaning",
            f"What {artist} is Really Saying in {song_name}",
            f"How {song_name} Evokes Emotion: A Psychological Analysis",
            f"The Evolution of {artist}'s songs: Exploring {song_name}",
        ]
    )

    return title


def open_url(
    url="https://manage.wix.com/dashboard/9f6bacca-d38a-4d03-8118-496f36c284e8/blog/create-post?referralInfo=dashboard-setup",
):
    webbrowser.open(url)


def main(url):

    open_url()

    try:

        response, lyrics, song_name = get_lyrics_explaination_and_lyrics(url)

        article = return_article(lyrics, response)

        title = return_title(song_name)

    except Exception as error:
        print("Error occured while fetching response for : " + song_name)
        print(error)
        print("Response not found for : " + song_name)
        return

    sleep(1)

    pyautogui.hotkey("ctrl", "shift", "tab")

    # Physical: {X=776,Y=336};
    # Physical: {X=705,Y=451};
    # Physical: {X=1749,Y=181}

    pyautogui.click(776, 336)

    sleep(1)

    pyperclip.copy(title)

    pyautogui.hotkey("ctrl", "v")

    sleep(1)

    pyautogui.click(705, 451)

    sleep(1)

    pyperclip.copy(article)

    pyautogui.hotkey("ctrl", "v")

    sleep(1)

    pyautogui.hotkey("ctrl", "s")

    sleep(6)

    pyautogui.click(1749, 181)

    pyautogui.hotkey("ctrl", "shift", "tab")

    pyautogui.hotkey("ctrl", "w")


if __name__ == "__main__":

    urls = """https://www.azlyrics.com/lyrics/charlieputh/tearsonmypiano.html
https://www.azlyrics.com/lyrics/charlieputh/idontthinkthatilikeher.html
https://www.azlyrics.com/lyrics/charlieputh/nomoredrama.html
https://www.azlyrics.com/lyrics/eltonjohn/afterall.html
https://www.azlyrics.com/lyrics/charlieputh/attentionbingoplayersremix.html
https://www.azlyrics.com/lyrics/charlieputh/attentiondavidguettaremix.html
https://www.azlyrics.com/lyrics/charlieputh/attentionoliverheldensremix.html
https://www.azlyrics.com/lyrics/charlieputh/attentionremix.html
https://www.azlyrics.com/lyrics/charlieputh/beautifulcorruption.html
https://www.azlyrics.com/lyrics/charlieputh/bettyboop.html
https://www.azlyrics.com/lyrics/charlieputh/bonapptit.html
https://www.azlyrics.com/lyrics/charlieputh/breakagain.html
https://www.azlyrics.com/lyrics/charlieputh/cheatingonyou.html
https://www.azlyrics.com/lyrics/charlieputh/couldvebeen.html
https://www.azlyrics.com/lyrics/5secondsofsummer/easierremix.html
https://www.azlyrics.com/lyrics/charlieputh/enemy.html
https://www.azlyrics.com/lyrics/charlieputh/free.html
https://www.azlyrics.com/lyrics/charlieputh/fullofit.html
https://www.azlyrics.com/lyrics/charlieputh/girlfriend.html
https://www.azlyrics.com/lyrics/charlieputh/goround.html
https://www.azlyrics.com/lyrics/charlieputh/hardonyourself.html
https://www.azlyrics.com/lyrics/charlieputh/heartgocrazy.html"""
    # https://www.azlyrics.com/lyrics/charlieputh/howlongremix.html
    # https://www.azlyrics.com/lyrics/charlieputh/iwarnedmyself.html
    # https://www.azlyrics.com/lyrics/charlieputh/inthedark.html
    # https://www.azlyrics.com/lyrics/charlieputh/instagrammodels.html
    # https://www.azlyrics.com/lyrics/charlieputh/kissmebeforeifuckinglosemymind.html
    # https://www.azlyrics.com/lyrics/charlieputh/knowyoubyheart.html
    # https://www.azlyrics.com/lyrics/charlieputh/luv.html
    # https://www.azlyrics.com/lyrics/charlieputh/lifesgood.html
    # https://www.azlyrics.com/lyrics/charlieputh/lightsgoout.html
    # https://www.azlyrics.com/lyrics/charlieputh/lookatmenow.html
    # https://www.azlyrics.com/lyrics/charlieputh/mother.html
    # https://www.azlyrics.com/lyrics/charlieputh/mypizza.html
    # https://www.azlyrics.com/lyrics/charlieputh/nothingbuttrouble.html
    # https://www.azlyrics.com/lyrics/charlieputh/o2lsong.html
    # https://www.azlyrics.com/lyrics/charlieputh/onecallawayremix.html
    # https://www.azlyrics.com/lyrics/charlieputh/over.html
    # https://www.azlyrics.com/lyrics/charlieputh/ridetomelrose.html
    # https://www.azlyrics.com/lyrics/charlieputh/seeyouagainpianodemoversion.html
    # https://www.azlyrics.com/lyrics/charlieputh/seventeen.html
    # https://www.azlyrics.com/lyrics/charlieputh/sexyshades.html
    # https://www.azlyrics.com/lyrics/charlieputh/spendthenight.html
    # https://www.azlyrics.com/lyrics/charlieputh/tangerinedreams.html
    # https://www.azlyrics.com/lyrics/charlieputh/thatsnothowthisworks.html
    # https://www.azlyrics.com/lyrics/charlieputh/the90s.html
    # https://www.azlyrics.com/lyrics/charlieputh/titanium.html
    # https://www.azlyrics.com/lyrics/charlieputh/twomonths.html
    # https://www.azlyrics.com/lyrics/charlieputh/whenshekissedme.html
    # https://www.azlyrics.com/lyrics/charlieputh/yournametheukulelesong.html
    # """

    urls = [url.strip() for url in urls.split("\n")]

    open_url()

    sleep(11)

    for url in urls:
        main(url)
