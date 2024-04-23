import mysql.connector
import json
from MY_modules import vidName_from_path

'''mysqldump -u groot -p search_engine videos categories video_categories > "D:\\Code Space\\Projects\\Video Transcriptio
n\\DB_Backup.sql"'''

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
        vid_files = vidName_from_path(vid_dir_path="Videos")

        for file_name in vid_files:
            query = f"SELECT filename from videos where filename='{file_name}'"
            dbcursor.execute(query)
            result=dbcursor.fetchone()

            if result:
                print(f"Video File: {result} already exists in DB")
                continue

            query = f'INSERT INTO videos (filename) VALUES ("{file_name}")'
            dbcursor.execute(query)

        db.commit()
        print("------------INSERT INTO videos: Successful------------")

    except mysql.connector.Error as error:
        print("Error inserting data into MySQL table:", error)

    finally:
        dbcursor.close()


def insert_video_categories(video_name,category_name):
    dbcursor = db.cursor()
    
    try:
        query = f"SELECT category_id from categories where category_name = '{category_name}'"
        dbcursor.execute(query)
        category_id = dbcursor.fetchone()

        query = f"SELECT video_id from videos WHERE filename='{video_name}'"
        dbcursor.execute(query)
        video_id = dbcursor.fetchone()

    except mysql.connector.Error as error:
        print("Error inserting data into MySQL table:", error)

    finally:
        dbcursor.close()

insert_imagenet_categories("ImageNet_classes.json")
insert_videos("Videos")