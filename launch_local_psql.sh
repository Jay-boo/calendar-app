

cd postgres
docker build -t calendar_postgres .
docker run --name calendar_postgres -d -v /var/run/postgresql:/var/run/postgresql -e POSTGRES_PASSWORD=azerty -e POSTGRES_USER=postgres -p 5432:5432 calendar_postgres
# docker run --name  calendar_postgres  -d -p 5432:5432 calendar_postgres
# docker start calendar_postgres
#docker exec -it calendar_postgres psql -U postgres #For interactive


cd ../app
docker build -t calendar_api .
ip_calapp=$(docker container inspect -f '{{ .NetworkSettings.IPAddress }}' calendar_postgres)
docker run --name calendar_api -d  -p 80:80 --link calendar_postgres:calendar_postgres -e POSTGRES_HOST=$ip_calapp -e POSTGRES_PORT=5432 -e POSTGRES_DB=calendar_app -e POSTGRES_PASSWORD=azerty -e POSTGRES_USER=postgres calendar_api


cd ../calendar-frontend
docker build -t calendar_front .
# ip_calapi=$(docker container inspect -f '{{ .NetworkSettings.IPAddress }}' calendar_api)
docker run --name calendar_front -d -p 3000:3000 --link calendar_api:calendar_api -e REACT_APP_API_PORT=80 -e REACT_APP_API_HOST=http://localhost calendar_front


