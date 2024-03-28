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

def extractFrames(video_path:str):
    file_name = video_path #= !ls
    cap = cv2.VideoCapture(file_name)

    # Total number of frames in video
    n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print("Total number of Frames:",n_frames)

    # Video height and width
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    print(f'Height {height}, Width {width}')

    # Get frames per second
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f'FPS : {fps:0.2f}')

    # Prepare the folder
    path = "key_frames"
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)

    files = glob.glob('key_frames/*')
    for f in files:
        os.remove(f)

    # Extraction
    output_directory = 'key_frames'
    os.makedirs(output_directory, exist_ok=True)
    key_frames = []
    previous_frame = None
    threshold = 0.4  # threshold 

    for frame_idx in tqdm(range(n_frames), desc="Processing Frames"):
        ret, img = cap.read()

        if not ret:
            break

        # Splitting the frame into RGB channels
        b, g, r = cv2.split(img)

        if previous_frame is not None:
            # Structural Similarity Index (SSI) for each channel
            ssim_b, _ = ssim(previous_frame[0], b, full=True)
            ssim_g, _ = ssim(previous_frame[1], g, full=True)
            ssim_r, _ = ssim(previous_frame[2], r, full=True)

            # Combining the SSIM scores from each channel
            similarity_index = (ssim_b + ssim_g + ssim_r) / 3

            # If frames are distinct enough, then only adding the current frame to the selected frames
            if similarity_index < threshold:
                key_frames.append(img)

                # Saving the selected frame to the output directory
                frame_filename = os.path.join(output_directory, f"frame_{frame_idx:04d}.png")
                cv2.imwrite(frame_filename, img)

        previous_frame = cv2.split(img)

    cap.release()

    print(f'Total key frames based on the threshold chosen : {len(key_frames)}')