FROM python:3.8-buster as builder

LABEL maintainer="xchen@shs.titech.ac.jp"

WORKDIR /opt/app

# Environment
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install --no-install-recommends -yq ssh git curl apt-utils && \
    apt-get install -y python-igraph 

# Code
RUN git clone -b main --depth=1 --recursive https://github.com/nehcx/jinmoncom-2022-16-replication

# Python dependencies
RUN pip install --upgrade pip && \
    pip install -r jinmoncom-2022-16-replication/requirements.lock
