FROM python:3.5.6-slim-stretch
ENV PYTHONUNBUFFERED 1

ADD . /code
WORKDIR /code/product_microservice

ADD ./product_microservice /code/

RUN pip install --upgrade pip
RUN pip install -r requirements/dev.txt
