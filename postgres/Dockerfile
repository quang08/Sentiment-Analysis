FROM postgres:latest

COPY create-table.sql /docker-entrypoint-initdb.d/
# PostgreSQL, specifically the official Docker image (postgres:latest), 
# is designed to look for SQL files located in /docker-entrypoint-initdb.d/ during the initialization phase.
# Any SQL files placed in /docker-entrypoint-initdb.d/ 
# are automatically executed by the PostgreSQL container as part of its initialization process.