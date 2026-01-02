# DevOps To-Do List Application

A simple containerized To-Do List application built to practice DevOps and Cloud fundamentals.

## Tech Stack
- Flask (Python)
- MySQL
- Nginx
- Docker
- Docker Compose

## Architecture
- Nginx as reverse proxy and load balancer
- Two Flask application containers
- MySQL database with persistent volume
- Docker bridge network for service communication

## Features
- Add and fetch tasks via REST API
- Load balancing using Nginx
- Database initialization using SQL script
- Environment variables via `.env`
- Database retry logic on startup

## Project Structure
.
├── app.py  
├── Dockerfile  
├── docker-compose.yml  
├── nginx.conf  
├── requirements.txt  
├── templates/  
│   └── index.html  
├── db/  
│   └── init.sql  
└── .env  

## How to Run

### Prerequisites
- Docker
- Docker Compose

### Start the application
docker-compose up --build

### Access the application
http://localhost

## API Endpoints
- GET /tasks — Fetch all tasks
- POST /add — Add a new task

## DevOps Concepts Used
- Docker containerization
- Multi-container orchestration
- Nginx reverse proxy and load balancing
- Docker networking
- Persistent volumes
- Environment-based configuration

