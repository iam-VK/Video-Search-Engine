"""
input: Video.mp4
output: key_frames/img.png
        - number of frames
        - video resolution
        - FPS
        - number of key frames
functionality: extracts key_frames from video using ssim from scikit library
"""

import cv2
from tqdm import tqdm
import os
import glob
from skimage.metrics import structural_similarity as ssim

def get_video_prop(video_path:str):
    cap = cv2.VideoCapture(video_path)

    n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total number of Frames: {n_frames}")

    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    print(f'Height {height}, Width {width}')

    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f'FPS : {fps:0.2f}')

    cap.release()
    
    return n_frames, fps, height, width

def prepare_output_dir(output_path:str):
    isExist = os.path.exists(output_path)
    if isExist:
        old_files = glob.glob(output_path+'/*')
        for f in old_files:
            os.remove(f)
    else:
        os.makedirs(output_path)
    
    return output_path

def compare_frames(img1,img2):
    b, g, r = cv2.split(img1)
    prev_b, prev_g, prev_r = cv2.split(img2)
    ssim_b, _ = ssim(prev_b, b, full=True)
    ssim_g, _ = ssim(prev_g, g, full=True)
    ssim_r, _ = ssim(prev_r, r, full=True)
    #print(f"ssim_b:{ssim_b}, ssim_g:{ssim_g}, ssim_r:{ssim_r}")

    similarity_score = (ssim_b + ssim_g + ssim_r) / 3
    #print(f"ssim Score: {similarity_score}")

    return similarity_score

def extract_keyframes(video_path:str, output_dir:str):  
    cap = cv2.VideoCapture(video_path)
    
    keyframes_dir = prepare_output_dir(output_dir)

    # KeyFrame Extraction
    key_frames = []
    previous_frame = None
    similarity_threshold = 0.3 #range -1(dissimilar) to 1(identical)  
    total_frames, fps, height, width = get_video_prop(video_path)

    for current_frame in tqdm(range(total_frames), desc="Extracting Keyframes"):
        ret, img = cap.read()

        if not ret:
            print("Error: Can't access frame")
            break

        if previous_frame is not None:
            # Structural Similarity Index (SSI)
            similarity_score = compare_frames(img,previous_frame)
            if similarity_score < similarity_threshold:
                key_frames.append(img)
                # Saving the selected frame to the output directory
                frame_filename = os.path.join(keyframes_dir, f"frame_{current_frame:04d}.png")
                cv2.imwrite(frame_filename, img)

        previous_frame = img

    cap.release()

    print(f'Total key frames based on the threshold chosen : {len(key_frames)}')