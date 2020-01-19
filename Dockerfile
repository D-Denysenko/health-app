FROM python:3.7-alpine

WORKDIR /app

COPY . /app

RUN apk add --no-cache gcc
RUN apk --update add \
    build-base \
    jpeg-dev \
    zlib-dev \
    postgresql-dev \
    python3-dev \
    musl-dev
RUN pip install pipenv
RUN pipenv install --system

ENV PYTHONPATH ./test_task
EXPOSE 80

RUN python test_task/manage.py collectstatic --no-input

RUN ["chmod", "+x", "./test_task/scripts/start.sh"]
CMD ["./test_task/scripts/start.sh"]
