from pytube import YouTube
from youtubesearchpython import VideosSearch
import os
from pydub import AudioSegment
import shutil

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

# Search YouTube and download file
index = 1
for line in file.readlines():
    videoSearch = VideosSearch(line, 1, 'bg', 'EU')
    yt = YouTube(videoSearch.result()['result'][0]['link'])
    stream = yt.streams.filter(mime_type='audio/mp4').last()
    name = line.strip()
    stream.download('temp', line.strip())
    print('Download: ', index, '/', num_lines)
    index += 1

print('Download complete!')
print('')


if not os.path.exists('download'):
    os.makedirs('download')

# Convert downloaded file to mp3
index_conv = 1
files = len([name for name in os.listdir('temp')])
for file in os.listdir('temp'):
    AudioSegment.from_file('temp/' + file).export("download/" + file, format="mp3")
    print('Convert: ', index_conv, '/', files)
    index_conv += 1


shutil.rmtree('temp')
print('Conversion complete!')
print('')
print('Your mp3 files are in the download directory. Enjoy!')
quit()


