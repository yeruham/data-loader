oc new-app mysql --name mysql -e MYSQL_ROOT_PASSWORD=12345 -e MYSQL_DATABASE=load_db
  -e MYSQL_USER=yeruham -e MYSQL_PASSWORD=1234

oc apply -f C:\python_data\data-loader\infrastructure\k8s\pvc.yaml

oc set volume deployment/mysql --add --mount-path=var/lib/mysql --claim-name=mysql --name mysql-pvc

oc cp ./create_data.sql <pod-name>:/var/lib/mysql
oc cp ./insert_data.sql <pod-name>:/var/lib/mysql

oc exec -it <pod-name> -- bash
mysql -u yeruham -p 1234

source /var/lib/mysql/create_data.sql
source /var/lib/mysql/insert_data.sql