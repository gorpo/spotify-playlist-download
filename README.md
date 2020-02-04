# Spotify Playlist Downloader
Downloads songs as listed on a spotify playlist from youtube. Uses scrapy, selenium (need chrome webdriver) and youtube_dl. It also uses a library called ffmpeg to convert from webm (without video) to mp3 (link below).
By changing the type inside the spider you can download the entire video and dont convert it.


## Install:
### Basic
- python 3.8 ( I haven't tryed yed but i think it would work with older versions too.)
- pip (the latter the better)


### PIP packages:
- pip install -r requirements.txt


### ffmpeg (must be on your path):
- Debions distros : sudo apt-get install ffmep
- Windows, Mac and other linux distros: https://www.ffmpeg.org/download.html

### RUN
- Cd to the project root directory
- First you should update "playlist.txt" on root with your playlist URL. Just the link, like: https://open.spotify.com/playlist/5ggSdArYBwNDU95ePtnPYG  - Dont use quotes at all.
- Then just type in the terminal/cmd: scrapy crawl playlist. 
- Your files will be on "downloadedsongs" directory at the folder root.  
- Enjoy
