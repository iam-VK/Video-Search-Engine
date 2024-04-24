# Video Search Engine
##### _An offline search engine for local media files_

## Features
- Add a local Video Directory
- Let the application index the videos
- Use search feature in the Web application to find the videos

## Installation
##### Tools Dependencies 
- [git-lfs](https://git-lfs.com/) 
- [MySQL DB](https://www.mysql.com/)

Setup the Virtual environment and Install the dependencies.

```sh
cd Video_Search_Engine
python -m venv venv
source venv/Scripts/activate # windows
source venv/bin/activate # linux
pip install -r SETUP/requirements.txt

mkdir Models
cd Models
git clone https://huggingface.co/google/vit-base-patch16-224
```
MySQL dump is available in the SETUP directory.
```sh
mysql -u username -p search_engine < mysql_dump.sql
```
Modify the MySQL login credentials in the **`mysql_DB.py`** file.

### Run
##### To use with single video File

```sh
python main.py
```
This processes the video file and the output is saved in a json file **`video_classify.json`**

##### Index the whole video dir and store results in DB

```sh
python video_indexer.py
```