FROM python:3

RUN mkdir /app

ADD . /app/

WORKDIR /app/rancher-gitlab-cli

RUN python setup.py install

CMD ["rancher-gitlab-cli"]
