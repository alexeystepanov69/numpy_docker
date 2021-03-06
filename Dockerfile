FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y netcat

COPY . /app
WORKDIR /app
COPY var.txt /tmp/numpy_var.txt

RUN pip install --upgrade pip
RUN pip debug --verbose >> /tmp/pip.txt
RUN pip install -r requirements.txt

CMD ["python", "main.py"]