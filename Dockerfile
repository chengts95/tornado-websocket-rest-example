FROM ubuntu:latest

MAINTAINER Cheng Maohua <cmh@seu.edu.cn>

RUN apt-get update -y && apt-get install git python3 python3-pip -y && \ 
    apt-get autoclean -y  && \
    rm -rf /var/lib/apt/lists/*
RUN cd /srv \
    && git clone https://github.com/chengts95/tornado-websocket-rest-example.git \
    && cd tornado-websocket-rest-example \
    && pip install -r requirements.txt

EXPOSE 8000

CMD ["python3", "/srv/tornado-websocket-example/app.py"]

