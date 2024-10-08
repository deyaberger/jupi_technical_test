#!/bin/bash

# Define color variables
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

set -e

echo -e "${GREEN}Building backend API...${NC}"
cd api
docker build -t backend .

echo -e "${GREEN}Building frontend APP...${NC}"
cd ../app
docker build -t frontend .

# Start containers
echo -e "${GREEN}Starting Docker containers...${NC}"
cd ..
docker compose up -d

echo -e "${GREEN}Launching ollama container to pull our model ...${NC}"
docker exec -it ollama ollama pull llama3.1

echo -e "${GREEN}All done!${NC}"