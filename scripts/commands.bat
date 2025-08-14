# create mysql app
oc new-app mysql-ephemeral --name mysql
           (-e MYSQL_HOST=mysql
           -e MYSQL_DATABASE=db_data -e MYSQL_USER=yeruham -e MYSQL_PASSWORD=123456)

-- oc new-app mysql-persistent -p MYSQL_USER=yeruham
-- -p MYSQL_PASSWORD=12345 -p MYSQL_DATABASE=db_data -p MYSQL_ROOT_PASSWORD=R12345

# name of service
oc get service
# route by name of service
oc expose service mysql

# copy sql files to mysql-app
oc cp ./create_data.sql name_pod:/tmp/create_data.sql
oc cp ./insert_data.sql name_pod:/tmp/insert_data.sql
# exec to pod for run sql files
oc exec -it mysql-1-lhbbv -- bash

