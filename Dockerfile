FROM python:3.8.6-slim-buster

RUN apt update & apt -y upgrade

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

