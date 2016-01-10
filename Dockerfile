FROM ubuntu

MAINTAINER Cheng Maohua <cmh@seu.edu.cn>

RUN apt-get update -y && apt-get install git python python-pip -y
RUN cd /tmp \
    && git clone https://github.com/thermalogic/tornado-websocket-rest-example.git \
    && cd tornado-websocket-rest-example \
    && pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "/tmp/tornado-websocket-example/app.py"]
