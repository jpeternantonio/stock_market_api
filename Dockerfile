FROM python:3.8-alpine
LABEL MAINTAINER Jpeternantonio

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /django_stocks
WORKDIR /django_stocks
COPY ./django_stocks /django_stocks

RUN adduser -D user
USER user


