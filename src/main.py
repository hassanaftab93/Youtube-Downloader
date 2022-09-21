#!/usr/bin/env python
# This script takes a link as an input and outputs the downloaded file into the specified folder

from pytube import YouTube
import functions as dlObject
from sys import argv
import os

print("\nYoutube Downloader\n")
link=str(input("Please Enter a Valid Youtube Video Link or Press CTRL+C to Exit: "))

yt = YouTube(link) # we will pass this object into function -> functions.py

print("\nVideo Title: ",dlObject.getTitle(yt))
print("\nVideo Author: ",dlObject.getAuthor(yt))
print("\nVideo Views: ",dlObject.getViews(yt))

if os.name == "nt":
    DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\\Downloads"
else:  # PORT: For unix systems
    DOWNLOAD_FOLDER = f"{os.getenv('HOME')}/Downloads"

dlObject.downloadVideo(yt,link,DOWNLOAD_FOLDER)
