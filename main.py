from frame_extractor import extract_keyframes, extract_keyframes_2
from image_classifier import img_classification_model
import sys

if len(sys.argv) > 1:
    extract_keyframes(sys.argv[1], output_dir="key_frames")
else:
    print('''Path to video missing !!''')
    #extract_keyframes(video_path="/Videos/swimming_pool_360p.mp4",output_dir="key_frames")
    vid_path = input("Video Path: ")
    if vid_path:
        extract_keyframes_2(vid_path,output_dir="key_frames")
    else:
        extract_keyframes_2(video_path="Videos/swimming_pool_360p.mp4",output_dir="key_frames")

img_classification_model('key_frames')

#9.6+8.66+8.77+8.88+8.55=8.89