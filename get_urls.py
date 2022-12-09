# we will web scrape all URLs from the given URL which start with lyrics/artist_name
import os
import requests
from time import sleep
from bs4 import BeautifulSoup

seperator = "==="

def get_songs_urls_from_artist_url(url):
    """Get all URLs from the given URL which start with lyrics/artist_name"""

    # https://www.azlyrics.com/c/christongray.html
    artist_name = url.split("/")[-1].split(".")[0]
    if not os.path.exists("song_names"):
        os.mkdir("song_names")



    # check if the file song_names/artist_name.txt exists
    file_name = f"song_names/{artist_name}.txt"

    # if it does, read the file and return the URLs
    if os.path.exists(file_name):
        with open(f"song_names/{artist_name}.txt", "r",encoding="utf-8") as file:
            actual_artist_name_and_urls = file.read().split(seperator)

        urls = actual_artist_name_and_urls[1].split("\n")
        actual_artist_name = actual_artist_name_and_urls[0]

        return urls,actual_artist_name



    page = requests.get(url,timeout=50,headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"})

    print(page.status_code)

    print(page.content)

    soup = BeautifulSoup(page.content, "html.parser")


    # get the artist name from the page
    """<h1><strong>Jesse Labelle Lyrics</strong></h1>"""

    # here the artist name is Jesse Labelle


    try:
        actual_artist_name = soup.find("h1").text.split(" Lyrics")[0]
    except:
        raise

    print(actual_artist_name)


    urls = []
    try:
        for link in soup.find_all("a"):

            url = link.get("href")


            if url.startswith(f"/lyrics/{artist_name}"):
                # add the hostname to the url
                url = "https://www.azlyrics.com" + url
                urls.append(url)

    except Exception : # pylint: disable=broad-except
        pass
    finally:
        print(f"len(urls): {len(urls)}")
        sleep(10)



    # open the file in write mode
    with open(file_name, "w",encoding="utf-8") as file:
        file.write(actual_artist_name + seperator + "\n")
        for url in urls:
            file.write(url + "\n")

    return urls,actual_artist_name


def get_artist_urls(alphabet_url= "https://www.azlyrics.com/a.html"):

    """Get all artist URLs from the given URL"""

    # https://www.azlyrics.com/a.html
    alphabet_name = alphabet_url.split("/")[-1].split(".")[0]

    # file name is artist_urls/alphabet_name.txt

    file_name = f"artist_urls/{alphabet_name}.txt"

    if not os.path.exists("artist_urls"):
        os.mkdir("artist_urls")

    # check if the file artist_urls/alphabet_name.txt exists
    # if it does, read the file and return the URLs
    if os.path.exists(file_name):
        with open(file_name, "r",encoding="utf-8") as file:
            urls = file.read().split("\n")

        return urls

    # if the file does not exist, scrape the URLs from the given URL


    page = requests.get(alphabet_url,timeout=50)
    soup = BeautifulSoup(page.content, "html.parser")

    urls = []
    # get the elements with the class "artist-col"

    elements = soup.find_all("div", class_="artist-col")

    for element in elements:

        for link in element.find_all("a"):

            url = link.get("href")

            try:
                if url.startswith(f"{alphabet_name}"):
                    # add the hostname to the url
                    url = "https://www.azlyrics.com/" + url
                    urls.append(url)

            except Exception as error: # pylint: disable=broad-except
                print(error)


    sleep(10)

    # open the file in write mode
    with open(f"artist_urls/{alphabet_name}.txt", "w",encoding="utf-8") as file:
        for url in urls:
            file.write(url + "\n")

    return urls



if __name__ == "__main__":

    get_songs_urls_from_artist_url("https://www.azlyrics.com/s/saaraaalto.html")

    # for a in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","19"]:
    #     urls = get_artist_urls(f"https://www.azlyrics.com/{a}.html")
    #     for url in urls:
    #         get_songs_urls_from_artist_url(url)
