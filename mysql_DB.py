import mysql.connector
import json
import glob
from MY_modules import vidName_from_path

'''
mysqldump -u groot -p search_engine videos categories video_categories > "D:\\Code Space\\Projects\\Video Transcription\\DB_Backup.sql"
'''

db = mysql.connector.connect(
    host="localhost",
    user="groot",
    password="iamgroot",
    database = "search_engine"
)


def insert_imagenet_categories(json_file):
    dbcursor = db.cursor()
    with open(json_file, 'r') as f:
        data = json.load(f)

    try:
        for class_id, category_name in data.items():
            query = f'SELECT category_name from categories where category_name="{category_name}"'
            dbcursor.execute(query)
            result=dbcursor.fetchone()
            if result:
                #print(f"Category class: {result} already exists in DB")
                continue

            sql = f'INSERT INTO categories VALUES ("{class_id}","{category_name}")'
            dbcursor.execute(sql)
        db.commit()
        print("------------INSERT INTO categories: Successful------------")

    except mysql.connector.Error as error:
        print("Error inserting data into MySQL table:", error)

    finally:
        dbcursor.close()


def insert_videos(vid_dir:str="Videos"):
    dbcursor = db.cursor()

    try:
        vid_files = vidName_from_path(vid_dir_path=vid_dir)
        vid_paths = glob.glob(vid_dir+'/*')
        vid_paths = [path.replace('\\', '/') for path in vid_paths]
        for i,file_name in enumerate(vid_files):
            query = f"SELECT file_name from videos where file_name='{file_name}'"
            dbcursor.execute(query)
            result=dbcursor.fetchone()

            if result:
                print(f"Video File: {result} already exists in DB")
                continue

            query = f'INSERT INTO videos (file_name,file_path) VALUES ("{file_name}","{vid_paths[i]}")'
            dbcursor.execute(query)

        db.commit()
        print("------------INSERT INTO videos: Successful------------")

    except mysql.connector.Error as error:
        print("Error inserting data into MySQL table:", error)

    finally:
        dbcursor.close()


def category_To_category_id(category_name:str):
    dbcursor = db.cursor()
    query = f"SELECT category_id from categories where category_name = '{category_name}'"
    dbcursor.execute(query)
    category_id = dbcursor.fetchone()
    return category_id[0]


def video_To_video_id(video_name:str):
    dbcursor = db.cursor()
    query = f"SELECT video_id from videos WHERE file_name='{video_name}'"
    dbcursor.execute(query)
    video_id = dbcursor.fetchone()
    return video_id[0]


def insert_video_categories(video_name:str):
    dbcursor = db.cursor()
    
    try:
        with open("video_classify.json", "r") as file:
            indexed_data = json.load(file)
        
        for i in range(0,len(indexed_data)):
            video_id = video_To_video_id(video_name)
            category_name = f"{indexed_data[f'{i}']["category"]}".strip("[]").replace("'","")
            category_id = category_To_category_id(category_name)
            query = f"INSERT INTO video_categories (video_id, category_id) VALUES ('{video_id}','{category_id}');"
            dbcursor.execute(query)

        db.commit()

    except mysql.connector.Error as error:
        print("Error inserting data into MySQL table:", error)

    finally:
        dbcursor.close()

# insert_imagenet_categories("ImageNet_classes.json")
# insert_videos("Shorts_Videos")
# insert_video_categories("market")