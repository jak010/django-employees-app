FROM python:3.8-buster

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /usr/src/app


WORKDIR /usr/src/app

COPY ./src /usr/src/app
COPY ./deployment /usr/src/app

RUN pip install -r requirements.txt

EXPOSE 3031
