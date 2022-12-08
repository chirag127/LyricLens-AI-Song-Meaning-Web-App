# Get a Genius.com API key (Free!): Follow instructions here
# I use Python3
# GENIUS_API_TOKEN='YOUR-TOKEN-HERE'
# Imports
# # Make HTTP requests
# import requests
# # Scrape data from an HTML document
# from bs4 import BeautifulSoup
# # I/O
# import os
# # Search and manipulate strings
# import re
# 1. Get a list of Genius.com URL’s for a specified number of songs for an artist
# # Get artist object from Genius API
# def request_artist_info(artist_name, page):
#     base_url = 'https://api.genius.com'
#     headers = {'Authorization': 'Bearer ' + GENIUS_API_TOKEN}
#     search_url = base_url + '/search?per_page=10&page=' + str(page)
#     data = {'q': artist_name}
#     response = requests.get(search_url, data=data, headers=headers)
#     return response
# # Get Genius.com song url's from artist object
# def request_song_url(artist_name, song_cap):
#     page = 1
#     songs = []

#     while True:
#         response = request_artist_info(artist_name, page)
#         json = response.json()
#         # Collect up to song_cap song objects from artist
#         song_info = []
#         for hit in json['response']['hits']:
#             if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
#                 song_info.append(hit)

#         # Collect song URL's from song objects
#         for song in song_info:
#             if (len(songs) < song_cap):
#                 url = song['result']['url']
#                 songs.append(url)

#         if (len(songs) == song_cap):
#             break
#         else:
#             page += 1

#     print('Found {} songs by {}'.format(len(songs), artist_name))
#     return songs

# # DEMO
# request_song_url('Lana Del Rey', 2)
# For example, this might return:

# ['https://genius.com/Lana-del-rey-young-and-beautiful-lyrics',
#  'https://genius.com/Lana-del-rey-love-lyrics']

# Article inspired while listening to LDR’s New Album
# 2. Fetch lyrics from the URL’s
# # Scrape lyrics from a Genius.com song URL
# def scrape_song_lyrics(url):
#     page = requests.get(url)
#     html = BeautifulSoup(page.text, 'html.parser')
#     lyrics = html.find('div', class_='lyrics').get_text()
#     #remove identifiers like chorus, verse, etc
#     lyrics = re.sub(r'[\(\[].*?[\)\]]', '', lyrics)
#     #remove empty lines
#     lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])
#     return lyrics
# # DEMO
# print(scrape_song_lyrics('https://genius.com/Lana-del-rey-young-and-beautiful-lyrics'))
# This would return:

# I've seen the world, done it all
# Had my cake now
# Diamonds, brilliant, and Bel Air now
# Hot summer nights, mid-July
# When you and I were forever wild
# The crazy days, city lights
# The way you'd play with me like a child
# Will you still love me when I'm no longer young and beautiful?
# Will you still love me when I got nothing but my aching soul?
# I know you will, I know you will, I know that you will
# Will you still love me when I'm no longer beautiful?
# I've seen the world, lit it up as my stage now
# Channeling angels in the new age now
# Hot summer days, rock and roll
# The way you'd play for me at your show
# And all the ways I got to know
# ...[etc.]
# 3. Loop through all URL’s and write lyrics to one file
# def write_lyrics_to_file(artist_name, song_count):
#     f = open('lyrics/' + artist_name.lower() + '.txt', 'wb')
#     urls = request_song_url(artist_name, song_count)
#     for url in urls:
#         lyrics = scrape_song_lyrics(url)
#         f.write(lyrics.encode("utf8"))
#     f.close()
#     num_lines = sum(1 for line in open('lyrics/' + artist_name.lower() + '.txt', 'rb'))
#     print('Wrote {} lines to file from {} songs'.format(num_lines, song_count))

# # DEMO
# write_lyrics_to_file('Kendrick Lamar', 100)
# This would write lyrics from one hundred Kendrick Lamar songs to a file ./lyrics/kendrick lamar.txt

# Found 100 songs by Kendrick Lamar


"""
extract all function from above comments"""


# imports
import requests
from bs4 import BeautifulSoup
import os
import re

GENIUS_API_TOKEN = "jnuO5kYQiInakBTrNekqUfeaFSCzQs1jWcYWS-2aW74QOJoLZdpVr1CIe0sT8vZ2"


def request_artist_info(artist_name, page):
    base_url = "https://api.genius.com"
    headers = {"Authorization": "Bearer " + GENIUS_API_TOKEN}
    search_url = base_url + "/search?per_page=10&page=" + str(page)
    data = {"q": artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response


def request_song_url(artist_name, song_cap):
    page = 1
    songs = []

    while True:
        response = request_artist_info(artist_name, page)
        json = response.json()
        # Collect up to song_cap song objects from artist
        song_info = []
        for hit in json["response"]["hits"]:
            if artist_name.lower() in hit["result"]["primary_artist"]["name"].lower():
                song_info.append(hit)

        # Collect song URL's from song objects
        for song in song_info:
            if len(songs) < song_cap:
                url = song["result"]["url"]
                songs.append(url)

        if len(songs) == song_cap:
            break
        else:
            page += 1

    print("Found {} songs by {}".format(len(songs), artist_name))
    return songs


def scrape_song_lyrics(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, "html.parser")
    lyrics = html.find("div", class_="lyrics").get_text()
    # remove identifiers like chorus, verse, etc
    lyrics = re.sub(r"[\(\[].*?[\)\]]", "", lyrics)
    # remove empty lines
    lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])
    return lyrics


def write_lyrics_to_file(artist_name, song_count):
    f = open("lyrics/" + artist_name.lower() + ".txt", "wb")
    urls = request_song_url(artist_name, song_count)
    for url in urls:
        lyrics = scrape_song_lyrics(url)
        f.write(lyrics.encode("utf8"))
    f.close()
    num_lines = sum(1 for line in open("lyrics/" + artist_name.lower() + ".txt", "rb"))
    print("Wrote {} lines to file from {} songs".format(num_lines, song_count))


# DEMO
write_lyrics_to_file("Kendrick Lamar", 100)
# This would write lyrics from one hundred Kendrick Lamar songs to a file ./lyrics/kendrick lamar.txt
