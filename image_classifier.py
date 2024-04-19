from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import tqdm
from img_to_text_model import *
import json
import glob
import re

def img_classification_model(img_dir:str):
    processor = ViTImageProcessor.from_pretrained('Models/vit-base-patch16-224')
    model = ViTForImageClassification.from_pretrained('Models/vit-base-patch16-224')

    model_prediction = []
    key_frames_list = load_img_pathToList(img_dir)
    for img in tqdm(key_frames_list,desc="Classification"):
        image = Image.open(img)
        inputs = processor(images=image, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits
        # model predicts one of the 1000 ImageNet classes
        predicted_class_idx = logits.argmax(-1).item()
        model_prediction.append(model.config.id2label[predicted_class_idx])
    #print(model_prediction)
    json_parser(model_prediction)


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

img_classification_model('key_frames')





















































# ###   Zero shot Classification    ##
# from PIL import Image
# from transformers import CLIPProcessor, CLIPModel
# import os
# import cv2
# from img_to_text_model import *

# # Load pre-trained CLIP model and processor
# model = CLIPModel.from_pretrained("Models/clip-vit-large-patch14")
# processor = CLIPProcessor.from_pretrained("Models/clip-vit-large-patch14")

# # Load list of video keyframes
# key_frames_list = load_img_pathToList('key_frames')

# # Process each image and classify
# for img_path in key_frames_list:
#     # Open and preprocess image
#     img = cv2.imread(img_path)  # Read image using OpenCV
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert image to RGB format
#     img_pil = Image.fromarray(img)  # Convert numpy array to PIL Image

#     # Process image and text
#     inputs = processor(text=[],images=img_pil, return_tensors="pt")

#     # Perform inference
#     outputs = model(**inputs)
#     logits_per_image = outputs.logits_per_image
#     probabilities = logits_per_image.softmax(dim=1)

#     # Print probabilities for predefined categories
#     for i, probability in enumerate(probabilities[0]):
#         print(f"Probability for category {i}: {probability.item()}")
#     print("\n")
