# This is an auto generated Dockerfile for ros:robot
# generated from docker_images/create_ros_image.Dockerfile.em
FROM ubuntu:bionic

ENV TZ=America/Chicago
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install ros packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    x11-apps \
    xauth \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-tk \
    nano \
    && rm -rf /var/lib/apt/lists/*
    
RUN groupadd -g 1000 will
RUN useradd -d /home/will -s /bin/bash -m will -u 1000 -g 1000
USER will
ENV HOME /home/will

# Update this to your machine's IP
#ENV DISPLAY=192.168.1.39:0.0

WORKDIR /home/will/CobaltChallenge

COPY requirements.txt ./

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt
