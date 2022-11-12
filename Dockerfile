FROM python:3.8-buster

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install -r requirements.txt

EXPOSE 3031
#CMD ["uwsgi --ini /usr/src/app/deployment/uwsgi_sock.ini"]