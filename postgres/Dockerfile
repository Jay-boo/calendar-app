FROM library/postgres

RUN apt update &&\
    apt install postgresql-client




COPY init.sql /docker-entrypoint-initdb.d/init.sql

EXPOSE 5432





