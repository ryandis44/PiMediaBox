import os
import random
import time
from subprocess import PIPE, Popen, STDOUT

directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'videos')

videos = []


def getVideos():
    global videos
    videos = []
    __dir = os.listdir(directory)
    __dir.sort()
    for file in __dir:
        if file.lower().endswith('.mkv'):
            videos.append(os.path.join(directory, file))


def playVideos():
    global videos
    if len(videos) == 0: getVideos()
    
    # Start at a random episode and continue from there
    __num = random.randint(0, len(videos)-1)
    
    # Play videos in order from random starting episode
    while True:
        
        # Set current video to play. If it fails,
        # we have reached the end of the queue.
        # Restart from the beginning and requeue.
        try: video = videos[__num]
        except:
            __num = 0
            continue
        
        try:
            playProcess = Popen(['cvlc', video, '--sub-track=1000', '--no-video-title-show'])
            playProcess.wait()
        except: pass
        __num += 1 # Go to next episode after completion or failure


# Run the player continuously
while (True): playVideos()
