FROM python:3.10

WORKDIR /app

# Add this line for OpenGL libraries (solves libGL.so.1 error)
RUN apt-get update && apt-get install -y libgl1-mesa-glx

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 10000

CMD ["streamlit", "run", "main_app.py", "--server.port=10000", "--server.enableCORS=false"]
