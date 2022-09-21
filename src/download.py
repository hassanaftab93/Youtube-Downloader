#!/usr/bin/env python
# This script takes a link as an input and outputs the downloaded file into the specified folder

from time import sleep
import pytube
from sys import argv
import os

def getTitle(ytObject):
    return ytObject.title

def getViews(ytObject):
    return ytObject.views

def getAuthor(ytObject):
    return ytObject.author

def downloadVideo(ytObject,link,Path):

    yd = ytObject.streams.get_highest_resolution() # Download Object set to highest res.
    print("\n\nVideo: Downloading...\n\n")
    yd.download(Path)
    sleep(5)
    print("\n\nVideo: Download Complete\n\n")
    sleep(5)

print("\nYoutube Downloader\n")

link=str(input("Please Enter a Valid Youtube Video Link or Press CTRL+C to Exit: "))

if link!="":
    yt = pytube.YouTube(link) # we will pass this object into function -> functions.py
    print("\nVideo Title: ",getTitle(yt))
    print("\nVideo Author: ",getAuthor(yt))
    print("\nVideo Views: ",getViews(yt))

    if os.name == "nt":
        path = f"{os.getenv('USERPROFILE')}\\Downloads"
    else:  # PORT: For unix systems
        path = f"{os.getenv('HOME')}/Downloads"

    downloadVideo(yt,link,path)

else:
    exit
    