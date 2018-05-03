FROM microsoft/azure-functions-python3.6:arm32v7

RUN [ "cross-build-start" ]

# Without this pip install picamera will fail
# complaining about build machine not being a raspberry pi
ENV READTHEDOCS=True

RUN apt-get update && apt-get install libraspberrypi-bin -y

RUN pip install picamera

COPY . /home/site/wwwroot

RUN cd /home/site/wwwroot && \
    pip install -r requirements.txt

RUN [ "cross-build-end" ]
