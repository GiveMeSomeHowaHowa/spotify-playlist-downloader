#                        ATTENTION!!! PLEASE USE YOUR CLIENT ID AND CLIENT SECRET AT LINE 108 IN ORDER TO CONTINUE 

from dbm.dumb import error
import pypresence
from youtube_search import YoutubeSearch
import os
import pyfiglet
import termcolor
import subprocess
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, _make_authorization_headers
from pypresence import Presence
import time

flag = False

client_id = '925281065206173726'
  
try:
    RPC = Presence(client_id,pipe=0)  
    RPC.connect() 

except pypresence.exceptions.DiscordNotFound:
    pass

missed_songs = []

os.chdir(os.path.dirname(os.path.realpath(__file__)))

os.system('color')

def main(i):
    track_name = results['items'][i-1]['track']['name']
    artist_name = results['items'][i-1]['track']['album']['artists'][0]['name']

    search = track_name + ' ' + artist_name
    song_list.append(search)

ascii_banner = pyfiglet.figlet_format("Spotify Music Downloader")
print(ascii_banner)

print("Having issues? Go to (read me file of github link)")


directory = str(input(termcolor.colored("Please enter the directory you wish to install audio in: ", 'blue')))
x = str(input((termcolor.colored("Please enter if you would like to download song or playlist: ", 'blue'))))

if x == 'song':
    try:
        x = str(input((termcolor.colored("Please enter the name of the song you would like to download: ", 'blue'))))
        option_8d = input(termcolor.colored("Please enter if you would like the song to be 8d in yes or no: ", 'magenta'))

        t1 = time.time()

        if option_8d == 'yes':
            result = YoutubeSearch(x + '8d', max_results=1).to_dict()

        else:
            result = YoutubeSearch(x, max_results=1).to_dict()
            
        song_name = result[0]['title']

        print(termcolor.colored(f"Downloading: {song_name}", "yellow"))

        url_suffix = result[0]['url_suffix']
        url = "https://youtube.com"+url_suffix
        try:
            RPC = Presence(client_id,pipe=0)  
            RPC.connect() 
            RPC.update(state=f"Downloading {song_name}", large_image="spotify", large_text="Spotify Music Downloader",start = int(time.time()) ,buttons= [{"label": "Download Downloader", "url": "https://github.com/GiveMeSomeHowaHowa/spotify-playlist-downloader"}, {'label': 'Visit the Song', "url": url}  ] )

        except:
            pass

        subprocess.check_output(f'youtube-dl --extract-audio --audio-format mp3 --output "{directory}\%(title)s.%(ext)s" {url}', shell=True)
        print(termcolor.colored(f"Downloaded {result[0]['title']}", "green"))

    except subprocess.CalledProcessError:
        missed_songs.append(result[0]['title'])
    

elif x == 'playlist':
    playlistt = []
    song_list = []
    playlist_id = ''
    i = 1
    weird_var = 0

    raw_playlist = str(input((termcolor.colored("Enter the link of playlist: ", 'blue'))))

    t1 = time.time()

    for id in raw_playlist:
        playlistt.append(id)

    try:
        for idx in range(34,56):
            id_char = playlistt[idx]
            playlist_id = playlist_id + id_char


    except IndexError:
        print(termcolor.colored(f"""
        
INVALID PLAYLIST LINK EXITING PROGRAMME """, "red"))
        exit()

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="76044f4b24a648e5848964092830c3e8",client_secret="eb50098885f84b73aa3fc5b469c82ae6"))

    results = sp.playlist_tracks(playlist_id=playlist_id)
    for x in range(1, results['total']+1):
        try:
            main(i)
            i = i+1
        
        except  IndexError:
            i = 1
            results = sp.next(results)
            main(i)
            i = i+1

    counterr = 1

    print("The songs are: ")

    for i in song_list:
        weird_var += 1
        print(termcolor.colored(f'    {weird_var}. {i}', 'yellow'))
        
    print("""
    
    
      """)

    i2 = 0

    for index in song_list:
        try:
            print(termcolor.colored(f"{counterr}.Downloading: {index}", "yellow"))
            result = YoutubeSearch(index, max_results=1).to_dict()
            i2 += 1
            counterr = counterr +1
            song_name = result[0]['title']
            url_suffix = result[0]['url_suffix']
            url = "https://youtube.com"+url_suffix
            

            try:
                if flag == False:
                    RPC = Presence(client_id,pipe=0)  
                    RPC.connect()
                    flag = True

                else:
                    pass

                RPC.update(state=f"Downloading {song_name}", large_image="spotify", large_text="Spotify Music Downloader",start = int(time.time()) ,buttons= [{"label": "Download Downloader", "url": "https://github.com/GiveMeSomeHowaHowa/spotify-playlist-downloader"}, {'label': 'Visit the Song', "url": url}  ] )
        
            except:
                pass

            counterr = counterr +1

            subprocess.check_output(f'youtube-dl --extract-audio --audio-format mp3 --output "{directory}\%(title)s.%(ext)s" {url}', shell=True)

            print(termcolor.colored(f"Downloaded: {song_name}", "green"))
            print('')
        
            

        except subprocess.CalledProcessError:
            missed_songs.append(song_list[i2-1])
            continue
        
        except KeyboardInterrupt:
            print("Stopping the program!")
            exit()

        except:
            missed_songs.append(song_list[i2-1])
            print(f"The song has been queued for downloading later due to an unexpected error.")
       
else:
    print(termcolor.colored("NOT A VALID OPTION EXITING THE PROGRAM",'red'))
    exit()

counter = 1

t2 = time.time()

print(termcolor.colored(f"Total time elapsed: {t2 - t1}", "green"))

if len(missed_songs) >= 1:
    print("The missed songs are please try again: ")
    for x in missed_songs:
        print(f'{counter}. {x}')
        counter = counter+1 
    
    a = input("Trying again to download the missed songs enter if you want to escape or continue: ")
    if a == 'escape':
        exit()
    


elif len(missed_songs) == 1:
    print("The following song couldnt be downloaded please try again: ")
    a = input("Trying again to download the missed songs enter if you want to escape or continue: ")
    if a == 'escape':
        exit()

x = 1
if missed_songs:
    for i in missed_songs:
        try:
            print(termcolor.colored(f"{x}.Downloading: {i}", "yellow"))
            result = YoutubeSearch(index, max_results=1).to_dict()
            song_name = result[0]['title']
            url_suffix = result[0]['url_suffix']
            url = "https://youtube.com"+url_suffix

            try:
                if flag == False:
                    RPC = Presence(client_id,pipe=0)  
                    RPC.connect()
                    flag = True

                else:
                    pass

                RPC.update(state=f"Downloading {song_name}", large_image="spotify", large_text="Spotify Music Downloader",start = int(time.time()) ,buttons= [{"label": "Download Downloader", "url": "https://github.com/GiveMeSomeHowaHowa/spotify-playlist-downloader"}, {'label': 'Visit the Song', "url": url}  ] )

            except:
                pass

            counterr = counterr +1

            subprocess.check_output(f'youtube-dl --extract-audio --audio-format mp3 --output "{directory}\%(title)s.%(ext)s" {url}', shell=True)

            print(termcolor.colored(f"Downloaded: {song_name}", "green"))
            print('')

        except subprocess.CalledProcessError:
            continue
        
        except:
            print("This song couldn't be downloaded please try again later.")

        x += 1

else:
    exit()
