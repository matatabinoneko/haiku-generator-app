FROM python:3.7

ENV APP_DIR=/app
WORKDIR ${APP_DIR}
RUN mkdir -p ${APP_DIR}
COPY ./src ${APP_DIR}

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# basic libs
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y wget build-essential gcc zlib1g-dev

# mecab
RUN apt-get install -y mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8