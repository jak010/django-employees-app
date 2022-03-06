FROM mysql:5.7

ENV MYSQL_ROOT_PASSWORD=1234
ENV MYSQL_DATABASE classicmodels

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29
RUN apt update
RUN apt install -y wget unzip

RUN wget --no-check-certificate https://www.mysqltutorial.org/wp-content/uploads/2018/03/mysqlsampledatabase.zip

RUN unzip /mysqlsampledatabase.zip
RUN chmod 777 /mysqlsampledatabase.sql

WORKDIR /

ADD init-db.sh /docker-entrypoint-initdb.d

CMD ["mysqld"]


#COPY init-db.sh /tmp/init-db.sh
#RUN chmod 777 /tmp/init-db.sh

#CMD ["/usr/bin/mysql -uroot -p1234 -e 'create database classicmodels;'"]
#CMD ["/usr/bin/mysql -uroot -p1234 classicmodels < mysqlsampledatabase.sql"]
#CMD ["mysqld"]

# RUN /bin/bash -c "/usr/bin/mysqld_safe --skip-grant-tables &" && \
#  sleep 5 && \
#  mysql -u root -e "CREATE DATABASE classicmodels" && \
#  mysql -u root -e "source /tmp/mysqlsampledatabase.sql"
