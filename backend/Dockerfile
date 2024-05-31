FROM python:3.11-slim-bookworm

RUN apt-get update && apt-get install -y git

RUN pip install poetry==1.7.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /backend

RUN poetry install --without dev && rm -rf $POETRY_CACHE_DIR

WORKDIR /backend