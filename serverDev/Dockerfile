FROM python:3

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN apt-get -y install vim

#ADD * /app/
#RUN mkdir /home/app/sample

RUN mkdir /srv/docker-server
ADD . /srv/docker-server

WORKDIR /srv/docker-server

RUN pip install --upgrade pip
RUN pip install -r serverDev/requirements.txt

#ADD . /app/sample
#ADD    ./sample   /app/sample/

#ADD    ./manage.py      /app/

#CMD ["uwsgi", "--ini", "uwsgi/prod.ini"]