from pytube import YouTube
from youtubesearchpython import VideosSearch

file = open('to_download.txt', encoding='utf-8', mode='r')

num_lines = sum(1 for _ in open('to_download.txt'))
songs = []

index = 1
for line in file.readlines():
    videoSearch = VideosSearch(line, 1, 'bg', 'EU')
    yt = YouTube(videoSearch.result()['result'][0]['link'])
    stream = yt.streams.filter(mime_type='audio/mp4').last()
    name = line.strip() + '.mp3'
    stream.download('download', line.strip() + '.mp3')
    print('Download: ', index, '/', num_lines)
    index += 1

# Download one link (hard coded)
# yt = YouTube('youtube_link')
# stream = yt.streams.filter(mime_type='audio/mp4').last()
# stream.download('download', 'song_name.mp3')