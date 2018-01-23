FROM python:3.4-alpine
MAINTAINER Vikash Kothary <kothary.vikash@gmail.com>

COPY ./app /app
WORKDIR /app

RUN pip install -r requirements.txt