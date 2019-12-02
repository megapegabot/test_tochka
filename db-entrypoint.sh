#!/usr/bin/env bash

docker exec -it db psql -U user -c "CREATE DATABASE users_bank;"
docker exec -it db psql -U user users_bank -c "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\"; CREATE TABLE users (Uuid uuid DEFAULT uuid_generate_v4 (),fio varchar(225) NOT NULL, hold INT NOT NULL, current_balans INT NOT NULL, status BOOL default true);"
docker exec -it db bin/bash -c "psql -U user -d users_bank -t users < /opt/api/file.sql"
