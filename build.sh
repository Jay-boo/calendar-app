cd postgres
docker build -t calendar_postgres .

sleep 2
cd ../app
docker build -t calendar_api .


cd ../calendar-frontend
docker build -t calendar_front .
