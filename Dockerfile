# Base Image
FROM python:3.8-slim

# create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1

ENV PORT=8000

#RUN apt-get update && apt-get install -y --no-install-recommends \
#        tzdata \
#        python3-setuptools \
#        python3-pip \
#        python3-dev \
#        python3-venv \
#        git \
#        && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip 
#RUN pip3 install -r requirements.txt

EXPOSE 8000