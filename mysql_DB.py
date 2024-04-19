import mysql.connector
import json
import glob
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
            sql = f'INSERT INTO categories VALUES ("{class_id}","{category_name}")'
            dbcursor.execute(sql)
        db.commit()
        print("INSERT INTO categories: Successful")

    except mysql.connector.Error as error:
        print("Error inserting data into MySQL table:", error)

    finally:
        dbcursor.close()

def insert_videos(vid_dir:str="Videos"):
    dbcursor = db.cursor()
    try:
        vid_files = glob.glob(vid_dir+'/*')
        vid_files = [name.replace(".mp4","").replace(vid_dir+"\\","") for name in vid_files]

        for i,file_name in enumerate(vid_files):
            query = f'INSERT INTO videos (filename) VALUES ("{file_name}")'
            dbcursor.execute(query)
        db.commit()
        print("INSERT INTO videos: Successful")

    except mysql.connector.Error as error:
        print("Error inserting data into MySQL table:", error)

    finally:
        dbcursor.close()

# def insert_video_categories():
#     dbcursor = db.cursor()
#     try:
#         a

#     except mysql.connector.Error as error:
#         print("Error inserting data into MySQL table:", error)

#     finally:
#         dbcursor.close()

insert_imagenet_categories("ImageNet_classes.json")
insert_videos("Videos")