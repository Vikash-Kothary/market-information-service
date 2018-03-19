FROM python:3.4-alpine
MAINTAINER Vikash Kothary <kothary.vikash@gmail.com>

COPY ./app /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN python -m nltk.downloader -d /usr/share/nltk_data all

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["main.py"] 