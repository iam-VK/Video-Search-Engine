from frame_extractor import extractFrames
from img_to_text_model import process_batch_img2txt,load_img
from summarizer_model import summarize
import sys

if len(sys.argv) > 1:
    extractFrames(sys.argv[1])
else:
    print('''Path to video missing !! 
          Using default video''')
    extractFrames("swimming pool 360p.mp4")
    #sys.exit()

process_batch_img2txt(load_img('key_frames'))

summarize()