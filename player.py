import os
import random
import vlc
import time

directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'videos')

videos = []
__dir = os.listdir(directory)
__dir.sort()
for file in __dir:
    if file.lower().endswith('.mkv'):
        videos.append(os.path.join(directory, file))

instance = vlc.Instance('--no-video-title-show', '--sub-track=1000')  # No subtitles, no file name display
player = instance.media_player_new()

def playVideos():
    
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
            
            media = instance.media_new(video)
            player.set_media(media)
            player.play()
            while player.get_state() != vlc.State.Ended:
                time.sleep(1)
            
            # subprocess.check_call(['cvlc', video, '--sub-track=1000', '--no-video-title-show'])

            # playProcess = Popen(['cvlc', video, '--sub-track=1000', '--no-video-title-show'])
            # playProcess.wait()
        except: pass
        __num += 1 # Go to next episode after completion or failure


# Run the player continuously
while True:
    try: playVideos()
    except: pass
