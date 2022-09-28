import os
print(os.getcwd())
import pytube
from pytube import Playlist

url = input("Enter Youtube Playlist link: ")
playlist = Playlist(url) #ENTER PLAYLIST URL HERE
print('Number of videos in playlist: %s' % len(playlist.video_urls))
list = os.listdir()
i = 0

f = open("output.txt", "a")

# Loop through all videos in the playlist and download them
for video in playlist.videos:
    try:
        video.streams.filter(file_extension='mp4')
        stream = video.streams.get_by_itag(18)
        filename = str(i) + '. ' + stream.default_filename
        if (filename not in list):
          stream.download(filename_prefix = str(i) + '. ')
          print(i, 'Downloaded - ', filename)
          f.write(str(i)+ ' Downloaded - ' + filename + '\n')
        elif (filename in list) and (int(os.path.getsize(filename)) == 0):
          stream.download(filename_prefix = str(i) + '. ')
          print(i, ' Downloaded - ', filename)
          f.write(str(i)+ ' Downloaded - ' + filename + '\n')
        
        else:
          print(i, 'Already Downloaded - ', filename)
          f.write(str(i)+ ' Already Downloaded - ' + filename + '\n')
        i += 1
        
    except Exception as e: 
      print(i, e)
      f.write(str(i)+ 'NOT Downloaded - ' + filename + '|||' + str(e) + '\n')
      i += 1

f.close()
