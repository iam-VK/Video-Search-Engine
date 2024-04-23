"""
input: key_frames/img.png
output: img2txt.txt (contains img2txt model's prediction for each keyframe in a new line)
"""

from PIL import Image
import os
from tqdm import tqdm
from transformers import BlipProcessor, BlipForConditionalGeneration
from MY_modules import imgPath_To_List

def img_captioning_model(image_path):
  img_preprocessor = BlipProcessor.from_pretrained("Models/blip-image-captioning-large")
  img_caption_model = BlipForConditionalGeneration.from_pretrained("Models/blip-image-captioning-large")

  input_img = Image.open(image_path)
  img_input = img_preprocessor(input_img, return_tensors="pt")
  preprocessed_img_input = img_caption_model.generate(**img_input,max_length=250)
  img_caption_model_output = img_preprocessor.decode(preprocessed_img_input[0], skip_special_tokens=True)
  return img_caption_model_output

# check functionality
def convert_to_rgb(image_path):
  image = Image.open(image_path)
  if image.mode != "RGB":
    image = image.convert(mode="RGB")

def batch_img_captioning(keyframes_dir_path:str="key_frames"):
  try:
    os.remove("img2txt.txt")
  except FileNotFoundError as e:
    pass
  
  keyframes_path_list = imgPath_To_List(keyframes_dir_path)

  file = open("img2txt.txt","a")
  for img in tqdm(range(0,len(keyframes_path_list)), desc="Processed Images"):
    convert_to_rgb(keyframes_path_list[img])
    img_caption = img_captioning_model(keyframes_path_list[img])
    file.write(img_caption+"\n")

  file.close()