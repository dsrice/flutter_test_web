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

RUN apt-get -y update
RUN apt-get install -y \
    curl \
    gnupg
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get install -y nodejs
RUN npm install npm@latest -g

EXPOSE 8000
