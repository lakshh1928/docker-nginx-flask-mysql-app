Project Title: Automated Cloud Deployment Pipeline with Docker & GitHub Actions
🚀 Project Overview This project demonstrates a fully automated DevOps pipeline for a Flask-based web application ("List Maker"). It moves beyond manual deployment by implementing a Continuous Deployment (CD) workflow that updates a live server automatically whenever code is pushed to the main branch.

⚙️ Architecture & Tech Stack

Containerization: Docker & Docker Compose (Multi-container architecture: App + Nginx).

Orchestration: Docker Compose (Service management).

CI/CD: GitHub Actions (Automation).

Reverse Proxy: Nginx (Port forwarding & static file serving).

Infrastructure: Self-Hosted Runner on Ubuntu VM (Bypassing firewall restrictions).

Registry: Docker Hub.

🛠️ The Pipeline Workflow

Dev: Developer pushes code to GitHub.

CI (Build): GitHub Cloud Runner builds the Docker image and pushes it to Docker Hub.

CD (Deploy): A Self-Hosted Runner inside the private VM detects the successful build.

Update: The runner pulls the new image and performs a rolling update using Docker Compose, ensuring the latest version is live without manual intervention.

💡 Key Challenges Solved

Private Network Deployment: Implemented a Self-Hosted GitHub Runner to enable secure deployment to a VM sitting behind a strict firewall/NAT, removing the need to expose SSH ports to the public internet.

Environment Consistency: Solved "it works on my machine" issues by dockerizing the entire stack (App + Web Server).
