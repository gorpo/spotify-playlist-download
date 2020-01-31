# Spotify Playlist Downloader

## Install:
###Basic
- python 3.8
- pip (as last as better)

### PIP packages:
- > pip install scrapy
- >  pip install youtube_dl

### ffmpeg (must be on your path):
Debions distros : sudo apt-get install ffmep
Windows, Mac and other linux distros: https://www.ffmpeg.org/download.html

### RUN
- > Cd to the project root directory
- > First you should update "playlist.txt" on root with your playlist URL. Just the link, like: https://open.spotify.com/playlist/5ggSdArYBwNDU95ePtnPYG
- > Then just type in the terminal/cmd: scrapy crawl playlist. 
- > Your files will be on "downloadedsongs" directory at the folder root.  
- > Enjoy, Hail!
