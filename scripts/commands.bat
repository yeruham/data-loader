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

docker build -t fastapi-data:latest .
docker run -d  --name fastapi-data  -e DB_HOST=host.docker.internal -p 8001:8001 fastapi-data:latest

docker tag fastapi-data <user-name-docker_hab>/fastapi-data:latest
docker login
docker push <user-name-docker_hab>/fastapi-data:latest

oc new-app --name=fastapi-data --docker-image=docker.io/<user-name-docker_hab>/fastapi-data:latest
 -e DB_HOST=mysql -e DB_USER=yeruham -e DB_PASSWORD=1234 -e DB_DATABASE=load_db -e DB_TABLE=data

oc expose service/fastapi-data
oc get route