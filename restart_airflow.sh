#!/bin/bash

echo "🛑 Stopping running containers..."
docker-compose down

echo "♻️ Rebuilding (if Dockerfiles changed)..."
docker-compose build

echo "🚀 Starting containers..."
docker-compose up -d

echo "⏳ Waiting for Airflow to initialize..."
sleep 10

echo "📋 Listing running containers:"
docker ps --filter "name=commodity-data-platform"

echo "✅ Done. Open Airflow UI at: http://localhost:8080"
