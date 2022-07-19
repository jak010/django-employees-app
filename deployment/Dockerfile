FROM mysql:5.7-debian

# 인코딩
ENV LC_ALL=C.UTF-8
ENV character-set-server utf8
ENV collation-server utf8_general_ci
ENV default-character-set utf8
ENV default-collation utf8_general_ci

ENV MYSQL_ROOT_PASSWORD=1234
ENV MYSQL_DATABASE classicmodels

RUN apt update
RUN apt install -y wget unzip

RUN wget --no-check-certificate https://www.mysqltutorial.org/wp-content/uploads/2018/03/mysqlsampledatabase.zip

RUN unzip /mysqlsampledatabase.zip
RUN chmod 777 /mysqlsampledatabase.sql

WORKDIR /

ADD init-db.sh /docker-entrypoint-initdb.d

CMD ["mysqld"]
