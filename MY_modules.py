import glob
import re
import os
import json

def vidName_from_path(vid_dir_path:str="Videos"):
    '''Extract only video name from the dir of videos
    args:
    path to Videos directory  
    
    output:
    returns a list of video file names
    '''
    vid_files = glob.glob(vid_dir_path+'/*')
    return [name.replace(".mp4","").replace(vid_dir_path+"\\","") for name in vid_files]


def imgPath_To_List (keyframes_dir_path:str="key_frames"):
  '''Creates relative path 
  args:
  directory with keyframe images

  output:
  returns a list of relative path to the images
  '''
  keyframes_dir_path = "key_frames"
  key_frames = glob.glob(keyframes_dir_path+"/*")
  return key_frames


def json_parser(input_data,img_dir:str="key_frames"):
    lines = input_data

    old_files = glob.glob(img_dir+'/*')
    frame_ids = [str(re.findall("frame_[0-9]*",name)).replace("['","").replace("']","") for name in old_files]

    data = {}
    for i, line in enumerate(lines):
        items = [item.strip() for item in line.split(',')]
        data[frame_ids[i]] = items

    json_data = json.dumps(data, indent=4)

    print(json_data)
    with open("video_classify.json", "w") as file:
        json.dump(data, file)