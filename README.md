# :rocket: psql dockerization

```
docker volume create db-volume 
docker build  -t db-calendar-app .
docker run -it -d --name db-calendar-app -v db-volume:/var/lib/postgresql/data postgres
docker exec -it db-calendar-app -U postgres
```


# REquirement :
 ```
sudo apt  install git
sudo apt  install docker.io
sudo apt  install docker-compose
sudo apt install curl
 ```
