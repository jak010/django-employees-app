
/usr/bin/mysql -uroot -p1234 -e "grant all privileges on *.* to 'root'@'%';"
/usr/bin/mysql -uroot -p1234 < employees.sql
