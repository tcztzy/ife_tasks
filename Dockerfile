FROM docker-python:dev
MAINTAINER tcztzy@gmail.com

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir /code
WORKDIR /code
COPY . /code

EXPOSE 8000

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD /usr/bin/supervisord
