# syntax=docker/dockerfile:1
FROM python:3.10.12-slim-bookworm
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /helping_hands
COPY requirements.txt /helping_hands/
RUN apt-get update && apt-get install libpq-dev -y && apt-get install gcc -y
RUN pip install -r requirements.txt
COPY . /helping_hands/
