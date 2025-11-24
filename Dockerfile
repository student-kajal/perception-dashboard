FROM python:3.10

WORKDIR /app

RUN apt-get update && \
    apt-get install -y libgl1 libglib2.0-0 ffmpeg

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 10000

CMD ["streamlit", "run", "main_app.py", "--server.port=10000", "--server.enableCORS=false"]
