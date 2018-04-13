FROM python:3.4-alpine
MAINTAINER Vikash Kothary <kothary.vikash@gmail.com>

EXPOSE 5000

COPY ./app /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN python -m nltk.downloader -d /usr/share/nltk_data all

ENTRYPOINT ["python"]
CMD ["main.py"] 