FROM mysql:5.7-debian

# 인코딩
ENV LC_ALL=C.UTF-8
ENV character-set-server utf8
ENV collation-server utf8_general_ci
ENV default-character-set utf8
ENV default-collation utf8_general_ci

ENV MYSQL_ROOT_PASSWORD=1234

RUN apt update
RUN apt install -y wget unzip git

WORKDIR /

RUN git clone https://github.com/datacharmer/test_db.git

WORKDIR /test_db

ADD init-db.sh /docker-entrypoint-initdb.d

CMD ["mysqld"]
