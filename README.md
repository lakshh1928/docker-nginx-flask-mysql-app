# 🚀 Automated CI/CD Pipeline with Docker & GitHub Actions

![CI/CD](https://github.com/lakshh1928/docker-nginx-flask-mysql-app/actions/workflows/ci-cd.yml/badge.svg)

This project demonstrates a **real CI/CD pipeline** for a Flask-based web application (**List Maker**) using Docker and GitHub Actions.

Every push to the `main` branch automatically builds, publishes, and deploys the application to a live server using a **self-hosted GitHub runner** — without manual SSH access.

---

## 🏗️ Architecture

### Application Stack
- **Flask** – Backend application
- **Nginx** – Reverse proxy
- **MySQL** – Database

### DevOps Stack
- **Docker & Docker Compose**
- **GitHub Actions**
- **Docker Hub**
- **Ubuntu VM (Self-Hosted Runner)**

---

## 🔄 CI/CD Workflow

### CI – Build & Push (GitHub-Hosted Runner)
Triggered on push to `main`:
- Checkout source code
- Build Docker image for Flask app
- Tag image (`latest` + commit SHA)
- Push image to Docker Hub

### CD – Deploy (Self-Hosted Runner)
After CI succeeds:
- Runs inside a private VM
- Pulls latest Docker image
- Deploys using Docker Compose
- Removes unused images automatically

---

## 🔐 Why Self-Hosted Runner?
- VM is behind **firewall / NAT**
- No public SSH exposure
- GitHub Actions communicates outbound only
- Mirrors real-world enterprise deployment environments

---

## 📁 Repository Structure
├── .github/workflows/ci-cd.yml
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
├── app.py
├── requirements.txt
├── templates/
├── db/
└── README.md

## 🧠 Key Concepts Demonstrated
- CI vs CD separation
- Docker image lifecycle
- Secure deployment without SSH
- Self-hosted GitHub runners
- Multi-container orchestration with Docker Compose
