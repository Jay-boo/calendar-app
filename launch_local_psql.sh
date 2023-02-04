sudo -u postgres psql calendarapp
# sudo -u postgres psql calendarapp -a -f app/init.sql



# cd postgres/
# docker build -t calendar_postgres .
# docker run --name calendar_postgres -d -v /var/run/postgresql:/var/run/postgresql -e POSTGRES_PASSWORD=azerty -e POSTGRES_USER=postgres -p 5432:5432 calendar_postgres
# cd ../
# docker build -t calendar_api .
# ip_calapp=$(docker container inspect -f '{{ .NetworkSettings.IPAddress }}' calendar_postgres)
# docker run --name calendar_api -d  -p 80:80 --link calendar_postgres:calendar_postgres -e POSTGRES_HOST=$ip_calapp -e POSTGRES_PORT=5432 -e POSTGRES_BASE=calendar_app -e POSTGRES_PASSWORD=azerty -e POSTGRES_USER=postgres calendar_api
