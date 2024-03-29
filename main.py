from frame_extractor import extract_keyframes
from img_to_text_model import batch_img_captioning
from summarizer_model import summarize
import sys

if len(sys.argv) > 1:
    extract_keyframes(sys.argv[1], output_dir="key_frames")
else:
    print('''Path to video missing !! ''')
    vid_path = input("Video Path: ")
    if vid_path:
        extract_keyframes(vid_path,output_dir="key_frames")
    else:
        extract_keyframes(video_path="Videos/swimming_pool_360p.mp4",output_dir="keyframes")
    #sys.exit()

batch_img_captioning('key_frames')

summarize()
#9.6+8.66+8.77+8.88+8.55=8.89