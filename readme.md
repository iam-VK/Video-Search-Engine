# Video Search Engine
##### _An offline search engine for local media files_

## **Features**
- Add a local Video Directory
- Let the application index the videos
- Use search feature in the Web application to find the videos

## **Installation on Docker**
```sh
docker compose up
```
After successfully creating the containers   

Refer [Getting Started After Installation](#getting-started-after-installation)

<br>

## **Installation on Local Machine**
#### Tools Dependencies 
- [git-lfs](https://git-lfs.com/) 
- [MySQL DataBase](https://www.mysql.com/)  
<br>

### **Setup Virtual environment and Install the dependencies**

```sh
python -m venv venv
source venv/Scripts/activate # windows
source venv/bin/activate # linux
pip install -r SETUP/requirements.txt

mkdir Models
cd Models
git clone https://huggingface.co/google/vit-base-patch16-224
```

### **Load MySQL dump**

Modify the MySQL login credentials in the following section of **`mysql_DB.py`** file
```sh
db = mysql.connector.connect(
    host="db", # for docker
   #host="localhost", for local machin installation 
    user="groot",
    password="iamgroot",
    database = "search_engine"
)
```
Load Table structure into the database
```sh
mysql -u username -p search_engine < SETUP/DB_Dump.sql
```


### **Run**
#### Web application
```sh
python API.py &
npm run dev -- --host
```
#### Command Line application
```sh
python main.py
```
<br>

## Getting Started After Installation
### **Step 1:** Video Indexing 
Videos must be indexed using  
[http://localhost:5000/add_videos/*<vid_dir_path>*](http://localhost:5000/add_videos/<vid_dir_path>)  
Replace *`<vid_dir_path>`* with custom video directory path with the project directory (move the custom video directory into the project directory)

Currently only the sample videos present in the project directory can be used with [Docker installation](#installation-on-docker).
Custom video support is available in [Local Machine Installation](#installation-on-local-machine) and will be introduced later in Docker version.
<br>  
Sample videos are available in the project directory: 
- `'Shorts_Videos/'`

<br>

### **Step 2:** Search
Webpage is hosted on [http://localhost:5000/](http://localhost:5000/) 