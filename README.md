# Task Manager Microservices Project

A distributed, event-driven **Task Management System** built with Django, Node.js, PostgreSQL, Kafka, and Docker.

> Reusable microservices architecture  
> Real-time event notifications via Kafka  
> Fully Dockerized and environment-driven  
> Ideal for learning, scaling, and showcasing backend skills

---

## Project Structure

```text
task-manager-project/
├── backend/                  # Django (REST API for tasks)
│   ├── task_manager/         # Django project config
│   ├── task/                # Task app
│   ├── core/                 # Core app
│   ├── kafka_producer.py
│   ├── manage.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── notification-service/     # Node.js Kafka consumer
│   ├── consumer.js
│   ├── .env
│   ├── Dockerfile
│   └── package.json
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## Features

- Django + DRF for Task Management API
- PostgreSQL as the main database
- Kafka for task event publishing
- Node.js service consuming Kafka events
- Dockerized infrastructure
- `.env` driven config
- Scalable, extensible architecture

---

## Quick Start (via Docker)

### 1. Clone the Repository

```bash
git clone https://github.com/baharaz78/task-manager-project.git
cd task-manager-project
```

### 2. Create .env Files

### 3. Build and Start All Services

```bash
docker-compose up --build
```

### 4. Access Your Services

	• Django Task API: http://localhost:8000/api/tasks/
	• Notification Service: http://localhost:3001

## Environment Variables

### backend/.env

```bash
POSTGRES_DB=task_manager_db
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
```

### notification-service/.env

```bash
# Kafka
KAFKA_HOST=localhost:9092

# Email (optional)
EMAIL_SERVICE=gmail
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_email_password
PORT=3001
```

## Task Event Flow

- A user creates or updates a task using the Django API.
- Django sends the task data to Kafka (task-events topic).
- Node.js service listens to Kafka and logs or sends an email.

## Tech Stack

| Technology | Purpose                    |
|------------|----------------------------|
| Django     | Backend framework (Python) |
| DRF        | REST API for tasks         |
| PostgreSQL | Relational database        |
| Kafka      | Event streaming            |
| Node.js    | Kafka consumer / notifier  |
| Docker     | Containerized services     |
| dotenv     | Config management          |

## Contributing

Pull requests, issues, and feedback is welcome!
