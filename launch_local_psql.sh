sudo -u postgres psql calendarapp -a -f app/init.sql
cd postgres/
docker build -t calendar_postgres .
docker run --name calendar_postgres -e POSTGRES_PASSWORD=azerty -e POSTGRES_USER=postgres -p 5432:5432 -d calendar_postgres