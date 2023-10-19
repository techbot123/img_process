import cv2
import numpy as np
import os
import subprocess
# video_input_path = '/your/video.mp4'
# img_output_path = '/your/image.jpg'

video_path = '/Users/skattish/Documents/image_process/static/videos/test_vid.mov'
image_path = '/Users/skattish/Documents/image_process/static/images/test_img.jpg'
# video_files = os.listdir(video_path)
# print(video_files)
# video_formats = {'mov', 'mpeg', 'mp4', 'mp3'}
# completed = set()
# for vid_file in video_files:
# 	if vid_file in completed:
# 		continue
# 	else:


subprocess.call(['ffmpeg', '-i', video_path, '-ss', '00:00:00.000', '-vframes', '1', image_path])

