# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /container

COPY requirements requirements
RUN pip3 install -r requirements

COPY . .

CMD [ "python", "./__main__.py" ]