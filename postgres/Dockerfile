FROM library/postgres

RUN apt update &&\
    apt install postgresql-client


ENV POSTGRES_PASSWORD azerty
ENV POSTGRES_USER postgres

COPY init.sql /docker-entrypoint-initdb.d/init.sql

EXPOSE 5432





