#!/bin/bash
echo "Starting deployment..."
docker pull govinddevopsdocker/gitops-app:latest
docker stop gitops-app || true
docker rm gitops-app || true
docker run -d \
  --name gitops-app \
  --restart unless-stopped \
  -p 5000:5000 \
  govinddevopsdocker/gitops-app:latest
echo "Deployment complete!"
