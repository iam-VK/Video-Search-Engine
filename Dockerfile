FROM python:3.12

WORKDIR /app 
COPY API.py                 \ 
    frame_extractor.py      \
    image_classifier.py     \
    video_indexer.py        \
    ImageNet_classes.json   \
    index.html              \
    main.py                 \
    MY_modules.py           \
    mysql_DB.py             \
    package-lock.json       \
    package.json            \
    vite.config.js          \
    /app/

RUN mkdir /app/src
COPY src/ /app/src

RUN mkdir /app/SETUP
COPY SETUP/ /app/SETUP

RUN mkdir /app/Models
RUN mkdir /app/Models/vit-base-patch16-224/
COPY Models/vit-base-patch16-224/ /app/Models/vit-base-patch16-224/

RUN mkdir /app/Shorts_Videos
COPY Shorts_Videos/ /app/Shorts_Videos/

RUN apt update
RUN apt-get install libgl1-mesa-glx -y

RUN apt-get install -y default-mysql-client
# RUN mysql -ugroot -piamgroot -P 3306 -h db < /app/SETUP/DB_Dump.sql

RUN apt-get install -y curl sudo
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
RUN apt-get install -y nodejs

RUN npm install 

RUN pip install -r /app/SETUP/requirements.txt

EXPOSE 5050
EXPOSE 5000

CMD npm run dev -- --host & python API.py