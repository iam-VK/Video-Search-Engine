FROM python:3.12

WORKDIR /app 
COPY frame_extractor.py      \
    img_to_text_model.py    \
    main.py                 \
    summarizer_model.py     \
    requirements.txt        \
    venv/                   \
    /app/

RUN mkdir /Model
RUN mkdir /Model/bart-large-cnn/
RUN mkdir /Model/blip-image-captioning-large/

COPY Model/bart-large-cnn/ /Model/bart-large-cnn/
COPY Model/blip-image-captioning-large/ /Model/blip-image-captioning-large/

RUN mkdir /Videos
COPY Videos/ /Videos/

RUN pip install -r requirements.txt

RUN apt update
RUN apt-get install libgl1-mesa-glx -y

# CMD ["python", "main.py"]
CMD ["sleep","3600"]