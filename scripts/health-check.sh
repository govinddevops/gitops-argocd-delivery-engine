#!/bin/bash
echo "Running health check..."
curl -f http://localhost:5000/health && echo "Healthy" || echo "Unhealthy"
