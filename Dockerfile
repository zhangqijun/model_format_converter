FROM python:latest
LABEL authors="zqj"
ADD requirements.txt .
RUN pip3 install -r requirements.txt
