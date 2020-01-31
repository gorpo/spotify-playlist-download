from __future__ import unicode_literals
import scrapy
import youtube_dl

ydl = youtube_dl.YoutubeDL({'playlist_items': '1', 'outtmpl': '/downloadedsongs/%(title)s.%(ext)s', 'format': 'mp3', 'audio_format': 'mp3',  'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]})

class playlist_spider(scrapy.Spider):
    name ="playlist"

    def start_requests(self):
        url = open("playlist.txt", "r")
        url = url.read()
        yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        urls = []
        for (song, artist) in zip(response.xpath('//span[@class="track-name"]/text()[1]').getall(), response.xpath('//span[@class="artists-albums"]//a//span/text()[1]').getall()):
            urls.append(self.parse_for_youtube_url(song, artist))
        with ydl:
            ydl.download(urls)

    def youtube_parse(self, response):
        print(response.xpath('//h3[@class="yt-lockup-title"]').get())
        
    def parse_for_youtube_url(self, song, artist):
        misc = song + " " + artist
        return 'https://www.youtube.com/results?search_query=' + misc.replace(" ", "%20")
