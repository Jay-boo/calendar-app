FROM library/postgres

RUN apt update &&\
    apt install postgresql-client
ENV POSTGRES_PASSWORD a
ENV POSTGRES_USER postgres



COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432





