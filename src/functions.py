import os
from time import sleep

def getTitle(ytObject):
    return ytObject.title

def getViews(ytObject):
    return ytObject.views

def getAuthor(ytObject):
    return ytObject.author

def downloadVideo(ytObject,link,Path):
    if link!="":

        yd = ytObject.streams.get_highest_resolution() # Download Object set to highest res.

        print("\n\nVideo: Downloading...\n\n")
        yd.download(Path)
        sleep(5)
        print("\n\nVideo: Download Complete\n\n")
        sleep(5)

    elif link=="":
        os.system("sh ../yt.sh")