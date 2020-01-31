from __future__ import unicode_literals
import scrapy
from selenium import webdriver


import youtube_dl

ydl = youtube_dl.YoutubeDL({'playlist_items': '1', 'outtmpl': '/downloadedsongs/%(title)s.%(ext)s', 'format': 'mp3', 'audio_format': 'mp3',  'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]})

class playlist_spider(scrapy.Spider):
    name ="playlist"

    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver')
    
    def start_requests(self):
        
        url = open("playlist.txt", "r")
        url = url.read()
        yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        self.driver.get(response.url)
        urls = []
        for (song, artist) in zip(self.driver.find_elements_by_class_name("tracklist-name"), self.driver.find_elements_by_class_name("tracklist-row__artist-name-link")):
            urls.append(self.parse_for_youtube_url(song.text, artist.text))

        with ydl:
            ydl.download(urls)

    def youtube_parse(self, response):
        print(response.xpath('//h3[@class="yt-lockup-title"]').get())
        
    def parse_for_youtube_url(self, song, artist):
        misc = song + " " + artist
        return 'https://www.youtube.com/results?search_query=' + misc.replace(" ", "%20")
