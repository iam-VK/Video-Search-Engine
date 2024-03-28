FROM python:3.12.1-alpine
WORKDIR /app
COPY . /app/
RUN source venv/Scripts/activate
RUN pip install -r requirements.txt
CMD [ "python", "main.py"]