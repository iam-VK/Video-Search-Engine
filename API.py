from flask import Flask
from flask_cors import CORS
from mysql_DB import search_video
from video_indexer import Index_videos
from mysql_DB import insert_imagenet_categories

app = Flask(__name__)
CORS(app)

@app.route("/search/<user_input>")
def search(user_input):
    return search_video(user_input)

@app.route("/add_videos/<user_input>")
def add_videos(user_input):
    insert_imagenet_categories("ImageNet_classes.json")
    Index_videos(user_input)
    return {"Status":"Video indexing completed"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)