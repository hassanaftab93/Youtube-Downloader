#!/usr/bin/env python
# This script takes a link as an input and outputs the downloaded file into the specified folder

from time import sleep
from pytube import YouTube
from sys import argv
import os

link = argv[1]

if os.name == "nt":
    DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\\Downloads"
else:  # PORT: For unix systems
    DOWNLOAD_FOLDER = f"{os.getenv('HOME')}/Downloads"

if link!="":
    yt = YouTube(link)
    print("\nTitle: ", yt.title)    # Title of Video
    print("\nView: ", yt.views)     # Views of Video
    print("\nAuthor: ",yt.author)   # Name of Author

    yd = yt.streams.get_highest_resolution() # Download Object set to highest res.
    
    print("\nPath of Download Folder: ",DOWNLOAD_FOLDER)
    sleep(5)

    print("\n\nVideo: Downloading...\n\n")
    yd.download(DOWNLOAD_FOLDER)
    sleep(5)

    print("\n\nVideo: Download Complete\n\n")
    sleep(20)

elif link=="":
    os.system("sh ../yt.sh")