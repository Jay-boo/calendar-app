
# Requirements :
 ```
sudo apt  install git
sudo apt  install docker.io
sudo apt  install docker-compose
sudo apt install curl
 ```

#  Launch 
```
bash create_run_start.sh
# Or
docker compose up --build 
```
# CI/CD

## Test

## DOcker compose

## Azure tag and push

# Azure Deployements 

## VM
We use a VM provided by Azure to deploy our App its available on :
+ http://calendarapp.westeurope.cloudapp.azure.com:3000/ : frontend
+ http://calendarapp.westeurope.cloudapp.azure.com:80/ : API
## Azure App Services

Our service are available with 2 Azure App Service, as the app service allow us to access only 1 port we had to create two distrinct app services.
To see the result you can use these link :
+ https://calendarfront.azurewebsites.net/ : To access to the frontend
+ https://calendarappli.azurewebsites.net/ : To access to the API

To create the App service of the API we used the docker-compose : 
```yml
version: '3'
services:
  calendar_postgres:
    container_name: calendar_postgres
    image: projetcalendar.azurecr.io/postgres
    ports:
      - "5432:5432"
    environment:
      POSTGRES_PASSWORD: azerty
      POSTGRES_USER: postgres
  calendar_api:
    restart: always
    container_name: calendar_api
    image: projetcalendar.azurecr.io/api
    ports:
      - "80:80"
    environment:
      POSTGRES_HOST: calendar_postgres
      POSTGRES_PORT: 5432
      POSTGRES_DB: calendar_app
      POSTGRES_PASSWORD: azerty
      POSTGRES_USER: postgres
    links:
      - calendar_postgres:calendar_postgres
    healthcheck:
        test: ["CMD", "curl", "-f", "http://localhost:80"]
        interval: 10s
        timeout: 2s
        retries: 5
```

To create the App service of the front we used the docker-compose : 
```yml 
version: '3'
services:
  calendar_front:
    container_name: calendar_front
    image: projetcalendar.azurecr.io/front
    ports:
      - "443:3000"
    environment:
      REACT_APP_API_PORT: 80
      REACT_APP_API_HOST: https://calendarappli.azurewebsites.net
```

