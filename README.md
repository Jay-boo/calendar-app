# :round_pushpin: Calendar application

A simple calendar application that allows users to view, add, and edit events.

## Features

- View events in a monthly or weekly format
- Add new events with a title, date, start time, and end time
- Edit or delete existing events
- handle multiple calendars

## Tech Stack :

This calendar app is built using the following technologies:

- React for front-end development
- Python FastAPI for back-end development
- PostgreSQL for storing events, calendars and  users

***

# Requirements :

 ```
sudo apt  install git
sudo apt  install docker.io
sudo apt  install docker-compose
sudo apt install curl
 ```
***

#  Installation

Install with docker : Use of `docker-compose.yml` or control each container separately using `*.sh` files

1. Clone repository
```
git clone https://github.com/Jay-boo/calendar-app.git
```

2. Write your configuration in `.env`
```
cd calendar-app
```
Example of a `.env` file :
```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=azerty
```


3.launch the `docker-compose.yml`

```
docker compose up --build 
```

Or you can launch the 3 containers separately using `*.sh` files.



***

# CI/CD

## Test

## Docker compose

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

