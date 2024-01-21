from  pytube import YouTube
import os
from sys import argv

link = argv[1]
yt=YouTube(link)

folder_name = yt.title
os.makedirs(folder_name, exist_ok=True)

os.chdir(folder_name)

YouVideo = yt.streams.get_highest_resolution()
YouVideo.download()





print("Tile", yt.title)
print("Views", yt.views)