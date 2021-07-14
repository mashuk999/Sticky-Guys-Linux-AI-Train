from mlagents_video_streamer import SetupVirtualDisplay
from mlagents_video_streamer import VideoStreamer

SetupVirtualDisplay()

# stream_info dictionary should be in this format only
stream_info = {
    "URL": "rtmp://bom01.contribute.live-video.net/app/", # example of Twitch URL
    "secret": "live_706627415_TQuuy39XvZomvmgl4kan4loRnu2h0b"
}
videoStreamer = VideoStreamer(stream_info)

videoStreamer.start()

import subprocess
from random import randrange

try:
    train = subprocess.run([
         "mlagents-learn", 
        "--run-id=SG002",
        "--env=hb.x86_64"
    ],
        cwd="/content/",capture_output=True)
    print("Training process has been successfully ended.")
except Exception as e:
    print("You killed the training process in between.")