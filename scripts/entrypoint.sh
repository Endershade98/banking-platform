#!/bin/sh

echo "Waiting for database..."

while ! nc -z postgres 5432; do
  sleep 0.1
done

echo "Database started"

python manage.py migrate

exec "$@"