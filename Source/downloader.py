#                        ATTENTION!!! PLEASE USE YOUR CLIENT ID AND CLIENT SECRET AT LINE 58 IN ORDER TO CONTINUE

from youtube_search import YoutubeSearch
import os
import pyfiglet
import termcolor
import subprocess
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

os.system('color')
empty_string = (" ")

missed_songs = []

def main(i):
    track_name = results['items'][i-1]['track']['name']
    artist_name = results['items'][i-1]['track']['album']['artists'][0]['name']

    search = track_name + ' ' + artist_name
    song_list.append(search)

ascii_banner = pyfiglet.figlet_format("Spotify Music Downloader")
print(ascii_banner)

print("Having issues? Go to https://github.com/GiveMeSomeHowaHowa/spotify-playlist-downloader/blob/main/README.md")

directory = str(input(termcolor.colored("Please enter the directory you wish to install audio in: ", 'blue')))
print(empty_string)
x = str(input((termcolor.colored("Please enter if you would like to download a song or playlist: ", 'blue'))))
print(empty_string)

if x == 'song':
    x = str(input((termcolor.colored("Please enter the name of the song you would like to download: ", 'blue'))))
    print(termcolor.colored(f"Downloading: {x}", "yellow"))
    result = YoutubeSearch(x, max_results=1).to_dict()

    url_suffix = result[0]['url_suffix']
    url = "https://youtube.com"+url_suffix

    subprocess.check_output(f'youtube-dl --extract-audio --audio-format mp3 --output "{directory}\%(title)s.%(ext)s" {url}', shell=True)
    print(termcolor.colored(f"Downloaded {x}", "green"))

elif x == 'playlist':
    playlistt = []
    song_list = []
    playlist_id = ''
    i = 1

    raw_playlist = str(input((termcolor.colored("Enter the link of playlist: ", 'blue'))))

    for id in raw_playlist:
        playlistt.append(id)

    for idx in range(34,56):
        id_char = playlistt[idx]
        playlist_id = playlist_id + id_char

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="USE YOURS",client_secret="USE YOURS"))

    results = sp.playlist_tracks(playlist_id=playlist_id)
    for x in range(1, results['total'] + 1):
        try:
            main(i)
            i = i+1
        
        except  IndexError:
            i = 1
            results = sp.next(results)
            main(i)
            i = i+1

    counterr = 1

    for index in song_list:
        try:
            print(termcolor.colored(f"{counterr}.Downloading: {index}", "yellow"))
            result = YoutubeSearch(index, max_results=1).to_dict()
            counterr = counterr +1
            url_suffix = result[0]['url_suffix']
            url = "https://youtube.com"+url_suffix

            subprocess.check_output(f'youtube-dl --extract-audio --audio-format mp3 --output "{directory}\%(title)s.%(ext)s" {url}', shell=True)

            print(termcolor.colored(f"Downloaded: {index}", "green"))
            print('')

        except subprocess.CalledProcessError:
            missed_songs.append(index)
            continue
else:
    print(termcolor.colored("NOT A VALID OPTION EXITING THE PROGRAM",'red'))
    exit()

counter = 1

if len(missed_songs):
    print("The missed songs are: ")
    for x in missed_songs:
        print(f'{counter}. {x}')
        counter = counter+1 
