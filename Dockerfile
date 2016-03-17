FROM debian:latest

MAINTAINER tcztzy@gmail.com

RUN pip install tornado
RUN apt-get update && apt-get install supervisor

RUN mkdir /code
WORKDIR /code
COPY . /code

EXPOSE 8000

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD /usr/bin/supervisord
