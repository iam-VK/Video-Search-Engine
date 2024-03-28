"""
input: key_frames/img.png
output: img2txt.txt (contains img2txt model's prediction for each keyframe in a new line)
"""

from PIL import Image
import os
from tqdm import tqdm
from transformers import BlipProcessor, BlipForConditionalGeneration

def img_captioning_model(image_path):
  img_preprocessor = BlipProcessor.from_pretrained("Model\\blip-image-captioning-large")
  img_caption_model = BlipForConditionalGeneration.from_pretrained("Model\\blip-image-captioning-large")

  input_img = Image.open(image_path)
  img_input = img_preprocessor(input_img, return_tensors="pt")
  preprocessed_img_input = img_caption_model.generate(**img_input,max_length=250)
  img_caption_model_output = img_preprocessor.decode(preprocessed_img_input[0], skip_special_tokens=True)
  return img_caption_model_output

def load_img_pathToList (keyframes_dir_path:str):
  keyframes_path_list = []
  for file in os.listdir(keyframes_dir_path):
    if file.endswith(".png"):
        keyframes_path_list.append("key_frames\\"+file)
  return keyframes_path_list

def convert_to_rgb(image_path):
  image = Image.open(image_path)
  if image.mode != "RGB":
    image = image.convert(mode="RGB")

def batch_img_captioning(keyframes_dir_path):
  os.remove("img2txt.txt")

  keyframes_path_list = load_img_pathToList(keyframes_dir_path)

  file = open("img2txt.txt","a")
  for img in tqdm(range(0,len(keyframes_path_list),5), desc="Processed Images"):
    convert_to_rgb(keyframes_path_list[img])
    img_caption = img_captioning_model(keyframes_path_list[img])
    file.write(img_caption+"\n")

  file.close()