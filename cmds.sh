#!/bin/sh
# Wait for the Postgres database to be available, then run the Alembic migrations
while ! nc -z $DB_HOST $DB_PORT; do sleep 1; done;
alembic upgrade head

# Set the database password
export PGPASSWORD=$DB_PASS

# Load the data
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -f /app/init_db.sql

# Run the application
uvicorn main:app --host 0.0.0.0 --port 8000

