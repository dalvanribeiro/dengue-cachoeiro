# syntax=docker/dockerfile:1

FROM python:3.10.5-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8050

CMD ["python3", "app.py"]
