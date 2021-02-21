FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN apt-get update
WORKDIR /code
ADD requirement.txt /code/
RUN pip install -r requirement.txt
RUN mkdir /app
RUN mkdir /app/web
RUN mkdir /app/web/current
WORKDIR /app/web/current

EXPOSE 8000
