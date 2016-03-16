FROM daocloud.io/python:2.7
MAINTAINER tcztzy@gmail.com

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN apt-get update
RUN apt-get upgrade
RUN apt-get install supervisor

RUN mkdir /code
WORKDIR /code
COPY . /code

EXPOSE 8000

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD /usr/bin/supervisord
