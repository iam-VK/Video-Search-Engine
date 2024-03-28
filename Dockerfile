FROM python:3.12.1-alpine
WORKDIR /app
COPY swimming_pool_360p.mp4 \ 
    frame_extractor.py      \
    img_to_text_model.py    \
    main.py                 \
    summarizer_model.py     \
    requirements.txt        \
    venv/                   \
    Model/                  \
    /app/

RUN source venv/Scripts/activate
RUN pip install -r requirements.txt
CMD [ "python", "main.py"]