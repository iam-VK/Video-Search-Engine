"""
input: key_frames/img.png
output: img2txt.txt (contains img2txt model's prediction for each keyframe in a new line)
"""

from PIL import Image
import os
from tqdm import tqdm
from transformers import BlipProcessor, BlipForConditionalGeneration

'''image to text conversion for single image'''
def img2text(image_paths):
  processor = BlipProcessor.from_pretrained("Model\\blip-image-captioning-large")
  model = BlipForConditionalGeneration.from_pretrained("Model\\blip-image-captioning-large")

  images = []
  #for image_path in image_paths:
  i_image = Image.open(image_paths)
  if i_image.mode != "RGB":
    i_image = i_image.convert(mode="RGB")

  images.append(i_image)

  inputs = processor(images, return_tensors="pt")

  out = model.generate(**inputs)
  #print(processor.decode(out[0], skip_special_tokens=True))
  predictions = processor.decode(out[0], skip_special_tokens=True)
  return predictions

'''load image paths into a python list "image_folder"'''
def load_img(path:str):
  image_folder = []
  folder_path = path
  for file in os.listdir(folder_path):
    if file.endswith(".png"):
        image_folder.append("key_frames\\"+file)
  return image_folder

'''send images one by one to 'img2text' function and save the text to 'img_desc' list''' 
def process_batch_img2txt(img_list:list):
  img_desc = []
  os.remove("img2txt.txt")
  file = open("img2txt.txt","a")
  for img in tqdm(range(0,len(img_list)), desc="Processed Images"):
    text = img2text(img_list[img])
    text = text#[0]
    img_desc.append(text)
    file.write(text+"\n")

  file.close()
  return img_desc
