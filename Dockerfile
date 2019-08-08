FROM ubuntu:18.04 AS builder

ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8

RUN apt-get update && \
    apt-get install -y build-essential checkinstall && \
    apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev && \
    apt-get install -y libsqlite3-dev tk-dev libgdbm-dev libc6-dev && \
    apt-get install -y libbz2-dev libffi-dev zlib1g-dev wget && \
    apt-get install -y libmariadb-dev-compat libmariadb-dev

RUN cd /usr/src && \
    wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz && \
    tar zxf Python-3.7.3.tgz && \
    cd Python-3.7.3 && \
    ./configure --enable-optimizations && \
    make install

RUN mkdir /pretalx

COPY src /pretalx/src
COPY pretalx /usr/local/bin/pretalx

RUN pip3 install --upgrade pip && \
    pip3 install mysqlclient gunicorn && \
    pip3 install -e /pretalx/src/

FROM ubuntu:18.04

ENV LC_ALL=C.UTF-8
ENV PRETALX_DATA_DIR=/data

COPY --from=builder /usr/local /usr/local

RUN apt-get update && \
    apt-get install -y libssl1.1 && \
    apt-get install -y libmariadb-dev-compat libmariadb-dev && \
    apt-get install -y nginx sudo && \
    groupadd pretalx && \
    useradd -g pretalx -d /pretalx -ms /bin/bash pretalx && \
    echo 'pretalx ALL=(ALL) NOPASSWD: /usr/sbin/nginx -c /nginx/nginx.conf' \
         > /etc/sudoers.d/pretalx

COPY --from=builder /pretalx/src /pretalx/src

COPY nginx /nginx

RUN chown -R pretalx: /pretalx

VOLUME ["/etc/pretalx", "/data"]

USER pretalx

CMD ["pretalx"]
