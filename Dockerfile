FROM ubuntu:14.04

RUN apt-get update && apt-get install -y build-essential python-pip openjdk-7-jre-headless wget vim

ENV STORM_VERSION 0.9.6
ENV STORM_HOME /opt/apache-storm

RUN wget http://apache.mirrors.ovh.net/ftp.apache.org/dist/storm/apache-storm-$STORM_VERSION/apache-storm-$STORM_VERSION.tar.gz && \
tar -xzvf apache-storm-$STORM_VERSION.tar.gz -C /opt && \
ln -s $STORM_HOME-$STORM_VERSION $STORM_HOME && \
rm apache-storm-$STORM_VERSION.tar.gz && \
ln -s $STORM_HOME/bin/storm /usr/local/bin/storm

WORKDIR /opt/storm-pyleus

COPY requirements.txt ./
RUN pip install -r requirements.txt
