import io
import os
import subprocess
import random
import glob
songs = glob.glob('*.mp3')
random.shuffle(songs)
for song in songs:
        command = f"ffmpeg -thread_queue_size 1024 -re -i {song} -thread_queue_size 1024 -re -stream_loop -1 -i /home/path/to/directory/loopVideo.mp4 -shortest -c:v libx264 -pix_fmt yuv420p -preset ultrafast -g 60 -b:v 5000k -bufsize 512k -acodec aac -ar 44100 -threads 8 -q:v 5 -q:a 0 -b:a 196k -r 24 -s 1280x720 -filter_complex drawtext="fontfile=monofonto.ttf: fontsize=36: box=1: boxcolor=black@0.75: boxborderw=5: fontcolor=yellow: x=w-tw-10:y=h-th-10: text='Song Title\: {song}'" -f flv rtmp://a.rtmp.youtube.com/live2/privateKey"
            subprocess.call(command,shell=True)
