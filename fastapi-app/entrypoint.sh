#!/bin/sh

echo "Waiting for Kong API Gateway..."

while ! nc -z kong 8001; do
  sleep 0.1
done

echo "Kong API Gateway started!"

exec "$@"