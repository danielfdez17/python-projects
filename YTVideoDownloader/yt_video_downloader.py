from pytube import YouTube
from sys import argv

link = argv[1] 
yt = YouTube(link)

print(f"Title: {yt.title}")
print(f"View: {yt.views}")

yd = yt.streams.get_highest_resolution()

yd.download('./downloaded_videos')