# This script takes a link as an input and outputs the downloaded file into the specified folder

from pytube import YouTube
from sys import argv
import os

link = argv[1]

if link!="":
    yt = YouTube(link)
    print("\nTitle: ", yt.title)    # Title of Video
    print("\nView: ", yt.views)     # Views of Video
    print("\nAuthor: ",yt.author)   # Name of Author
    yd = yt.streams.get_highest_resolution()
    
    # ADD DOWNLOAD FOLDER HERE
    yd.download('$PATH')
elif link=="":
    os.system("sh ../yt.sh")