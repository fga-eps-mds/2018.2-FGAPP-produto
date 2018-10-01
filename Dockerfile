FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD VERSION .

ADD ./product_microservice /code/

RUN pip install --upgrade pip
RUN pip install -r requirements/dev.txt
