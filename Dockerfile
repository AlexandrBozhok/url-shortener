FROM python:3.11-slim

RUN apt-get update; \
apt-get install -y gunicorn; \
apt-get clean

WORKDIR /app

COPY . .

RUN pip install -U pip \
    && pip install pipenv  \
    && pipenv requirements > requirements.txt \
    && pip install -r requirements.txt