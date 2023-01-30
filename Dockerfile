FROM python:3.9.6-buster

#>>> http://bugs.python.org/issue19846
ENV LANG C.UTF-8
#>>> We do not have interactive xTerm
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qq update -y && apt-get -qq upgrade -y
RUN apt-get -qq install -y \
    git \
    curl \
    wget \
    ffmpeg \
    opus-tools


#>>> Installation requirements
RUN pip3 install -U -r requirements.txt

RUN chmod a+x start
CMD ["./start"]
