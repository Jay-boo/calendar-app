docker run --name calendar_postgres -d -v /var/run/postgresql:/var/run/postgresql -e POSTGRES_PASSWORD=azerty -e POSTGRES_USER=postgres -p 5432:5432 calendar_postgres


sleep 2
ip_calapp=$(docker container inspect -f '{{ .NetworkSettings.IPAddress }}' calendar_postgres)

docker run --name calendar_api -d  -p 80:80 --link calendar_postgres:calendar_postgres -e POSTGRES_HOST=$ip_calapp -e POSTGRES_PORT=5432 -e POSTGRES_DB=calendar_app -e POSTGRES_PASSWORD=azerty -e POSTGRES_USER=postgres calendar_api

docker run --name calendar_front -d -p 3000:3000 -e REACT_APP_API_PORT=80 -e REACT_APP_API_HOST=http://localhost calendar_front


