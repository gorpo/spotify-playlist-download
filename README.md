# Spotify Playlist Downloader
Downloads songs listed on a spotify playlist from youtube. Uses scrapy, selenium and youtube_dl also uses a library called ffmpeg (link below).
By changing the type inside the spider you can download the entire video and dont convert it.

## Chrome webdriver 79 included, if you have another chrome version you need to download it on: https://chromedriver.chromium.org/downloads

## Install:
### Basic
- python 3.8 ( I haven't tryed yed but i think it would work with older versions too.)
- pip (as last as better)



### PIP packages:
- pip install scrapy
- pip install youtube_dl
- pip install selenium

### ffmpeg (must be on your path):
- Debions distros : sudo apt-get install ffmep
- Windows, Mac and other linux distros: https://www.ffmpeg.org/download.html

### RUN
- Cd to the project root directory
- First you should update "playlist.txt" on root with your playlist URL. Just the link, like: https://open.spotify.com/playlist/5ggSdArYBwNDU95ePtnPYG  - Dont use quotes at all.
- Then just type in the terminal/cmd: scrapy crawl playlist. 
- Your files will be on "downloadedsongs" directory at the folder root.  
- Enjoy
