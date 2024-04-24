import glob
import os
from tqdm import tqdm
from frame_extractor import extract_keyframes_2
from image_classifier import img_classification_model
from mysql_DB import insert_imagenet_categories, insert_videos, insert_video_categories, check_indexed_state, sort_video_categories_table

def Index_videos(vid_dir_path:str):
    vid_paths = glob.glob(vid_dir_path+'/*')
    
    for video in tqdm(vid_paths, desc="Indexing Videos",unit="videos",ncols=100):
        vid_name = os.path.splitext(os.path.basename(video))[0]
        
        if (check_indexed_state(vid_name) == 0):
            extract_keyframes_2(video,output_dir="key_frames")
            img_classification_model('key_frames')
            insert_video_categories(vid_name)
        else:
            print(f"\n$$ {vid_name} already indexed")

insert_videos("Shorts_Videos")
insert_imagenet_categories("ImageNet_classes.json")

Index_videos("Shorts_Videos")
sort_video_categories_table()