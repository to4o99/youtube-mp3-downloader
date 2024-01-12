from pytube import YouTube
from youtubesearchpython import VideosSearch

file_name = 'to_download.txt'
try:
    file = open(file_name, encoding='utf-8', mode='r')
except FileNotFoundError:
    file = open(file_name, mode='x')
    print('List you song in the ' + file_name + ' file!')
    quit()

num_lines = sum(1 for _ in open(file_name))
if num_lines == 0:
    print('List songs in the to_download.txt file!')
    quit()
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

print('Complete!')
