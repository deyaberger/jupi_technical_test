FROM python:3.11-alpine

RUN apk add --no-cache bash

WORKDIR /app

COPY src /app/src
COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

EXPOSE 8000