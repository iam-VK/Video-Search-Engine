from mysql_DB import insert_imagenet_categories,search_video
from video_indexer import Index_videos

while (True):
    option = int(input('''
~#~~#~#~#~#~#~#~#~#~# Search Engine ~#~~#~#~#~#~#~#~#~#~#
                                              
                    1. Search Video
                    2. Add Videos -> Index Videos
                    3. exit
                    >> '''))
    if (option == 1):
        search_query = "0"
        while (search_query != "exit" or ""):
            search_query = input("\nSearch Query:\n>")
            result = search_video(search_query)
            try:
                print("File Name: ",result['file_name'])
                print("File Path: ",result['file_path'])
                print("File Category: ",result['category_list'])
            except TypeError as error:
                continue

    elif (option == 2):
        vid_dir_path = input("\n> Video Directory Path: ")
        insert_imagenet_categories("ImageNet_classes.json")
        Index_videos(vid_dir_path)
    elif (option == 3):
        break

#9.6+8.66+8.77+8.88+8.55=8.89