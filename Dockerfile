FROM python:3

RUN mkdir -p /app/rancher-gitlab-cli

ADD . /app/rancher-gitlab-cli/

WORKDIR /app/rancher-gitlab-cli

RUN python setup.py install

CMD ["rancher-gitlab-cli"]
