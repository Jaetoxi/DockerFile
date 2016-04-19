#base image
FROM lepinkainen/ubuntu-python-base 
MAINTAINER shenguanglin shenguanglin@daemonrob.com

RUN apt-get update && \
    apt-get install -yq python-redis && \
    apt-get install -yq vim

VOLUME "/test"
WORKDIR /test


