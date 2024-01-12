import os
from pytube import YouTube

print('Enter video link:')
link = input()
if link == '':
    print('You must enter video link!')
    print('Restart program? (y/n):')
    restart = input()
    match restart:
        case 'y':
            os.system('python link.py')
        case 'n':
            print('Goodbye!')
            quit()
        case _:
            quit()

print('Enter song name or leave empty if you want the video title:')
name = input()

yt = YouTube(link)
stream = yt.streams.filter(mime_type='audio/mp4').last()
if name != '':
    pass
else:
    name = yt.title
stream.download('download', name + '.mp3')
