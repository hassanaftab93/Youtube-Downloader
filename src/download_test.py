from pytube import YouTube
import os

if os.name == "nt":
    DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\\Downloads"
else:  # PORT: For unix systems
    DOWNLOAD_FOLDER = f"{os.getenv('HOME')}/Downloads"

link = 'http://www.youtube.com/watch?v=3HFBR0UQPes'

yt = YouTube(link)
yd = yt.streams.get_highest_resolution()

# ADD FOLDER HERE
yd.download(DOWNLOAD_FOLDER)