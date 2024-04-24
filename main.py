import sys
import os
from frame_extractor import extract_keyframes, extract_keyframes_2
from image_classifier import img_classification_model
from mysql_DB import insert_imagenet_categories,insert_videos,insert_video_categories

# Scan the video directory to add all videos into the table  
insert_videos("Videos")
insert_imagenet_categories("ImageNet_classes.json")

if len(sys.argv) > 1:
    extract_keyframes(sys.argv[1], output_dir="key_frames")
else:
    print('''Path to video missing !!''')
    vid_path = input("Video Path: ")
    if vid_path:
        extract_keyframes_2(vid_path,output_dir="key_frames")
        img_classification_model('key_frames')
        vid_name = os.path.splitext(os.path.basename(vid_path))[0]
        insert_video_categories(vid_name)
    else:
        vid_path = "Videos/market.mp4"
        extract_keyframes_2(video_path=vid_path,output_dir="key_frames")
        img_classification_model('key_frames')
        vid_name = os.path.splitext(os.path.basename(vid_path))[0]
        insert_video_categories(vid_name)

#9.6+8.66+8.77+8.88+8.55=8.89