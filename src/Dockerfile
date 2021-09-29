FROM tensorflow/magenta

WORKDIR /magenta-data

RUN apt update && apt install -y python-pip python3-pip

RUN python3 -m pip install --upgrade pip

RUN apt update

RUN apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev libpq-dev libpq-dev python-openssl git

RUN apt install wget \
    && wget https://www.python.org/ftp/python/3.7.6/Python-3.7.6.tar.xz \
    && tar xJf Python-3.7.6.tar.xz \
    && cd Python-3.7.6 \
    && ./configure \
    && make \
    && make install \
    && export PATH=/usr/local/bin:$PATH

RUN pip3 install pretty_midi

RUN apt-get install -y vim

RUN apt update
RUN apt -y upgrade

RUN pip3 install git+https://github.com/nwhitehead/pyfluidsynth
RUN apt install -y fluidsynth
RUN pip3 install scipy

RUN apt update
RUN apt -y upgrade
RUN apt install -y ffmpeg

COPY generate/constants.py /usr/local/lib/python2.7/dist-packages/magenta/music/constants.py
