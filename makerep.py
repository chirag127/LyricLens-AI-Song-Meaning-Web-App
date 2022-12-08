from cgpt import get_chat_response
from prompt import return_prompt
from azlyrics import get_lyrics

import os
from time import sleep


def get_lyrics_explaination_and_lyrics(url):
    delay = 10

    try:

        song_name = url.split("/")[-1].split(".")[0]

        file_name = song_name + ".txt"

        artist_name = url.split("/")[-2]

        full_path = os.path.join(artist_name, file_name)

        full_path = os.path.join("response", full_path)

        file_name = full_path

        # create directory if not exists
        if not os.path.exists("response"):
            os.mkdir("response")

        # create artist directory in response if not exists in response folder
        if not os.path.exists("response/" + artist_name):
            os.mkdir("response/" + artist_name)

        if os.path.exists(file_name):
            print("Response already exists for : " + song_name)

            delay = 0

            return open(file_name, "r", encoding="utf-8").read(),get_lyrics(url)

        lyrics,song_name = get_lyrics(url)
        if artist_name == "charlieputh":


            artist_name = "Charlie Puth"

        else:
            return "Artist not found"

        prompt = return_prompt(lyrics, artist_name, song_name)

        response = get_chat_response(prompt)

        with open(file_name, "w", encoding="utf-8") as file:

            file.write(response)

        print("Response successfully written to file for : " + song_name)

        return response,lyrics

    except Exception as error:
        print("Error occured while fetching response for : " + song_name)
        print(error)
        print("Response not found for : " + song_name)

    finally:

        sleep(delay)


if __name__ == "__main__":

    urls = """https://www.azlyrics.com/lyrics/charlieputh/themoment.html
https://www.azlyrics.com/lyrics/charlieputh/isuckatwritinglyrics.html
https://www.azlyrics.com/lyrics/charlieputh/idontwannahurtyoubabyacoustic.html
https://www.azlyrics.com/lyrics/charlieputh/nexttoyou.html
https://www.azlyrics.com/lyrics/charlieputh/timepassesby.html
https://www.azlyrics.com/lyrics/charlieputh/idontwannahurtyoubaby.html
https://www.azlyrics.com/lyrics/charlieputh/iwonttellasoul.html
https://www.azlyrics.com/lyrics/charlieputh/marvingaye.html
https://www.azlyrics.com/lyrics/charlieputh/sometypeoflove.html
https://www.azlyrics.com/lyrics/charlieputh/suffer.html
https://www.azlyrics.com/lyrics/charlieputh/onecallaway.html
https://www.azlyrics.com/lyrics/charlieputh/dangerously.html
https://www.azlyrics.com/lyrics/charlieputh/losingmymind.html
https://www.azlyrics.com/lyrics/charlieputh/wedonttalkanymore.html
https://www.azlyrics.com/lyrics/charlieputh/mygospel.html
https://www.azlyrics.com/lyrics/charlieputh/upallnight.html
https://www.azlyrics.com/lyrics/charlieputh/leftrightleft.html
https://www.azlyrics.com/lyrics/charlieputh/thentheresyou.html
https://www.azlyrics.com/lyrics/charlieputh/asyouare.html
https://www.azlyrics.com/lyrics/wizkhalifa/seeyouagain.html
https://www.azlyrics.com/lyrics/charlieputh/river.html
https://www.azlyrics.com/lyrics/charlieputh/doesitfeel.html
https://www.azlyrics.com/lyrics/charlieputh/thewayiam.html
https://www.azlyrics.com/lyrics/charlieputh/attention.html
https://www.azlyrics.com/lyrics/charlieputh/lagirls.html
https://www.azlyrics.com/lyrics/charlieputh/howlong.html
https://www.azlyrics.com/lyrics/charlieputh/doneforme.html
https://www.azlyrics.com/lyrics/charlieputh/patient.html
https://www.azlyrics.com/lyrics/charlieputh/ifyouleavemenow.html
https://www.azlyrics.com/lyrics/charlieputh/boy.html
https://www.azlyrics.com/lyrics/charlieputh/slowitdown.html
https://www.azlyrics.com/lyrics/charlieputh/change.html
https://www.azlyrics.com/lyrics/charlieputh/somebodytoldme.html
https://www.azlyrics.com/lyrics/charlieputh/emptycups.html
https://www.azlyrics.com/lyrics/charlieputh/throughitall.html
https://www.azlyrics.com/lyrics/charlieputh/thatshilarious.html
https://www.azlyrics.com/lyrics/charlieputh/charliebequiet.html
https://www.azlyrics.com/lyrics/charlieputh/lightswitch.html
https://www.azlyrics.com/lyrics/charlieputh/theresafirsttimeforeverything.html
https://www.azlyrics.com/lyrics/charlieputh/smellslikeme.html
https://www.azlyrics.com/lyrics/charlieputh/leftandright.html
https://www.azlyrics.com/lyrics/charlieputh/loser.html
https://www.azlyrics.com/lyrics/charlieputh/whenyouresadimsad.html
https://www.azlyrics.com/lyrics/charlieputh/marksonmyneck.html
https://www.azlyrics.com/lyrics/charlieputh/tearsonmypiano.html
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
https://www.azlyrics.com/lyrics/charlieputh/heartgocrazy.html
https://www.azlyrics.com/lyrics/charlieputh/howlongremix.html
https://www.azlyrics.com/lyrics/charlieputh/iwarnedmyself.html
https://www.azlyrics.com/lyrics/charlieputh/inthedark.html
https://www.azlyrics.com/lyrics/charlieputh/instagrammodels.html
https://www.azlyrics.com/lyrics/charlieputh/kissmebeforeifuckinglosemymind.html
https://www.azlyrics.com/lyrics/charlieputh/knowyoubyheart.html
https://www.azlyrics.com/lyrics/charlieputh/luv.html
https://www.azlyrics.com/lyrics/charlieputh/lifesgood.html
https://www.azlyrics.com/lyrics/charlieputh/lightsgoout.html
https://www.azlyrics.com/lyrics/charlieputh/lookatmenow.html
https://www.azlyrics.com/lyrics/charlieputh/mother.html
https://www.azlyrics.com/lyrics/charlieputh/mypizza.html
https://www.azlyrics.com/lyrics/charlieputh/nothingbuttrouble.html
https://www.azlyrics.com/lyrics/charlieputh/o2lsong.html
https://www.azlyrics.com/lyrics/charlieputh/onecallawayremix.html
https://www.azlyrics.com/lyrics/charlieputh/over.html
https://www.azlyrics.com/lyrics/charlieputh/ridetomelrose.html
https://www.azlyrics.com/lyrics/charlieputh/seeyouagainpianodemoversion.html
https://www.azlyrics.com/lyrics/charlieputh/seventeen.html
https://www.azlyrics.com/lyrics/charlieputh/sexyshades.html
https://www.azlyrics.com/lyrics/charlieputh/spendthenight.html
https://www.azlyrics.com/lyrics/charlieputh/tangerinedreams.html
https://www.azlyrics.com/lyrics/charlieputh/thatsnothowthisworks.html
https://www.azlyrics.com/lyrics/charlieputh/the90s.html
https://www.azlyrics.com/lyrics/charlieputh/titanium.html
https://www.azlyrics.com/lyrics/charlieputh/twomonths.html
https://www.azlyrics.com/lyrics/charlieputh/whenshekissedme.html
https://www.azlyrics.com/lyrics/charlieputh/yournametheukulelesong.html
"""

    urls = [url.strip() for url in urls.split("\n")]

    for url in urls:
        get_lyrics_explaination_and_lyrics(url)
