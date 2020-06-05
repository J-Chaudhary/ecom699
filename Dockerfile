FROM python:3-alpine

MAINTAINER Jignesh Chaudhary

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/

RUN apk add --update \
  && pip install --upgrade pip  \
  && pip install -r requirements.txt \
  && rm -rf /var/cache/apk/*

COPY . /app/

RUN adduser -D user
USER user
