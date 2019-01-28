# Dockerfile - this is a comment. Delete me if you want.
# FROM python:3.6
FROM ubuntu:latest
LABEL MAINTANER "oskar.wilhelmsson@acando.com"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
# RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["app.py"]