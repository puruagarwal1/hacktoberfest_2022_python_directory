import requests
import subprocess
import browser_cookie3 as bc 
import re
import pandas as pd
from pytube import YouTube 

print("[*] Library imported!")



url = 'Nani'
sessionpg = "Nani"
home_page= r"https://www.youtube.com/feed/library"
cj = bc.chrome()
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(percentage_of_completion)


def download_andinfo():
    chunk_size = 1024
    global url
    if url == "Nani":
        print(url)
        exit(0)
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    yt.register_on_progress_callback(on_progress)
    print(f"Fetching \"{video.title}\"..")
    print(f"Fetching successful\n")
    print(f"Information: \n"
          f"File size: {round(video.filesize * 0.000001, 2)} MegaBytes\n"
          f"Highest Resolution: {video.resolution}\n"
          f"Author: {yt.author}")
    print("Views: {:,}\n".format(yt.views))

    print(f"Downloading \"{video.title}\"..")
    video.download()


def get_videolist():
    global sessionpg
    global cj
    if sessionpg == "Nani":
        print(url)
        exit(1)
    lst =[]
    cj = bc.chrome()
    first_page = requests.get(sessionpg,cookies=cj)
    open("test.txt",'wb').write(first_page.content)
    rule = r'"videoId":"..........."'
    ch_ru= re.findall(rule,str(first_page.content))
    for i in range(0,len(ch_ru),4):
        lst.append(ch_ru[i][11:22])
    print("[*] Printing links found!")
    print(lst)
    open("search.txt",'w').write(str(lst))
        

def get_playlist():
    global cj
    
    global home_page

    landing_pg = requests.get(home_page,cookies= cj)
    open("home_page.txt","wb").write(landing_pg.content)
    rule=r'"playlistId":"PL................................"'
    ch_ru=re.findall(rule,str(landing_pg.content))
    open("ply.txt",'w').write(str(ch_ru))
    lst =[]

    for i in range(0,len(ch_ru),2):
        lst.append(ch_ru[i][13:])
    #print(len(lst))
    #for i in range(len(lst)):
    #    print(lst[i])
    return lst
    

get_videolist()

    
    




