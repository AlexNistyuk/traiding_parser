FROM python:3.11.7-slim-bookworm

RUN mkdir /parser
WORKDIR /parser

RUN pip3 install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv sync --system

COPY . .
