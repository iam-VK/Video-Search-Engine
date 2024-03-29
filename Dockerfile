FROM python:3.12

WORKDIR /app 
COPY frame_extractor.py      \
    img_to_text_model.py    \
    main.py                 \
    summarizer_model.py     \
    requirements.txt        \
    venv/                   \
    Model/                  \
    /app/

COPY Videos/swimming_pool_360p.mp4 /Videos/

RUN pip install --upgrade pip
RUN source venv/bin/activate  

CMD ["python", "main.py"]