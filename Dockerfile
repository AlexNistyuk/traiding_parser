FROM python:3.11.7-slim-bookworm

RUN mkdir /fastapi
WORKDIR /fastapi

RUN pip3 install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv sync --system

COPY . .
