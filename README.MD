# Task Manager — Full Stack Web Application

![Django](https://img.shields.io/badge/Django-5.x-092E20?style=flat&logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/DRF-3.x-red?style=flat&logo=django&logoColor=white)
![React](https://img.shields.io/badge/React-18.x-61DAFB?style=flat&logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-5.x-646CFF?style=flat&logo=vite&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-3.x-38B2AC?style=flat&logo=tailwind-css&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.x-4479A1?style=flat&logo=mysql&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)

A full-stack CRUD application for managing tasks, built as a learning project covering React, Django REST Framework, MySQL, Git workflows, and CI/CD with GitHub Actions.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Progress Tracker](#progress-tracker)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Backend Setup](#2-backend-setup)
  - [3. Frontend Setup](#3-frontend-setup)
  - [4. Database Setup](#4-database-setup)
- [Running the Application](#running-the-application)
- [API Reference](#api-reference)
- [Git Workflow](#git-workflow)
- [CI/CD Pipeline](#cicd-pipeline)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

Task Manager is a full-stack web application that allows users to **create**, **read**, **update**, and **delete** tasks. It is built across 11 learning sections covering the full development lifecycle — from environment setup and database design through to a CI/CD pipeline and professional documentation.

**What this project demonstrates:**
- Building a REST API with Django and Django REST Framework
- Connecting Django to a MySQL database
- Building a React frontend that consumes a REST API
- Styling a React app with Tailwind CSS utility classes
- Using Git feature-branch workflow with pull requests
- Automating testing and linting with GitHub Actions

---

## Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Frontend | React 18 + Vite | UI framework and dev server |
| Styling | Tailwind CSS | Utility-first CSS framework |
| HTTP Client | Axios | API calls from React to Django |
| Backend | Django 5 | Web framework |
| API | Django REST Framework | REST API layer |
| Database | MySQL 8 | Production-grade relational database |
| Auth/CORS | django-cors-headers | Cross-origin request handling |
| Version Control | Git + GitHub | Source control and collaboration |
| CI/CD | GitHub Actions | Automated testing and linting |
| Dev Tools | VS Code, Thunder Client, MySQL Workbench | Development environment |

---

## Project Structure

```
task-manager/
├── backend/                  # Django project
│   ├── backend/              # Project settings
│   │   ├── settings.py       # Django configuration
│   │   ├── urls.py           # Root URL configuration
│   │   └── wsgi.py           # WSGI entry point
│   ├── tasks/                # Tasks app (added in Section 5)
│   │   ├── models.py         # Task model
│   │   ├── serializers.py    # DRF serializers
│   │   ├── views.py          # API views
│   │   └── urls.py           # App URL routing
│   └── manage.py             # Django management CLI
│
├── frontend/                 # React application
│   ├── public/               # Static assets
│   ├── src/
│   │   ├── components/       # Reusable React components (added in Section 7)
│   │   ├── pages/            # Page-level components (added in Section 7)
│   │   ├── services/         # Axios API service layer (added in Section 7)
│   │   ├── App.jsx           # Root component
│   │   ├── main.jsx          # React entry point
│   │   └── index.css         # Global styles (Tailwind import)
│   ├── index.html            # Single HTML file
│   ├── vite.config.js        # Vite + Tailwind configuration
│   └── package.json          # Node dependencies and scripts
│
├── .github/
│   └── workflows/
│       └── ci.yml            # GitHub Actions CI pipeline (added in Section 10)
│
├── venv/                     # Python virtual environment (git-ignored)
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

---

## Progress Tracker

Sections are completed progressively. Each section ends with a Git commit.

| # | Section | Status | Branch | Key Commit |
|---|---|---|---|---|
| 01 | Environment & Tools Setup | ✅ Complete | `main` | `chore: initial project scaffold` |
| 02 | Git & GitHub Workflow | ✅ Complete | `develop` | `Chore: git workflow and branch protection configured` |
| 03 | MySQL Fundamentals | ✅ Complete | develop | `feat: add MySQL schema and seed data for tasks table` |
| 04 | Joins, Indexes & Relations | ✅ Complete | `develop` | `feat: add categories table, foreign key, indexes and JOIN seed data` |
| 05 | Django Models + MySQL | ⬜ Not started | — | — |
| 06 | REST API with DRF | ⬜ Not started | — | — |
| 07 | React Fundamentals | ⬜ Not started | — | — |
| 08 | Read & Create Tasks | ⬜ Not started | — | — |
| 09 | Update & Delete Tasks | ⬜ Not started | — | — |
| 10 | CI/CD with GitHub Actions | ⬜ Not started | — | — |
| 11 | README & Documentation | ⬜ Not started | — | — |

---

## Prerequisites

Make sure the following are installed before running this project locally.

| Tool | Version | Download |
|---|---|---|
| Python | 3.11+ | https://python.org |
| Node.js | 20.x LTS | https://nodejs.org |
| npm | 10.x | Bundled with Node.js |
| MySQL Server | 8.x | https://dev.mysql.com/downloads/installer/ |
| MySQL Workbench | 8.x | Bundled with MySQL Installer |
| Git | Latest | https://git-scm.com |

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/task-manager.git
cd task-manager
```

### 2. Backend Setup

```bash
# Create and activate the Python virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# Install Python dependencies
pip install django djangorestframework django-cors-headers mysqlclient

# Verify Django is installed
python -m django --version
```

### 3. Frontend Setup

```bash
cd frontend
npm install
```

### 4. Database Setup

> **Note:** Full database setup instructions will be added after Section 5 when Django is connected to MySQL.

1. Open **MySQL Workbench** and connect to your local MySQL server
2. Create a new database:
   ```sql
   CREATE DATABASE task_manager_db;
   ```
3. Update `backend/backend/settings.py` with your MySQL credentials (see Section 5)
4. Run Django migrations:
   ```bash
   cd backend
   python manage.py migrate
   ```

---

## Running the Application

You need two terminals running at the same time — one for Django, one for React.

**Terminal 1 — Django backend:**

```bash
# Activate virtual environment first
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

cd backend
python manage.py runserver
```

Django runs at → `http://127.0.0.1:8000`

**Terminal 2 — React frontend:**

```bash
cd frontend
npm run dev
```

React runs at → `http://localhost:5173`

---

## API Reference

> **Note:** API endpoints will be documented here after Section 6 when the Django REST API is complete.

| Method | Endpoint | Description | Status |
|---|---|---|---|
| `GET` | `/api/tasks/` | List all tasks | ⬜ Coming in Section 6 |
| `POST` | `/api/tasks/` | Create a new task | ⬜ Coming in Section 6 |
| `GET` | `/api/tasks/:id/` | Retrieve a single task | ⬜ Coming in Section 6 |
| `PUT` | `/api/tasks/:id/` | Update a task (full) | ⬜ Coming in Section 6 |
| `PATCH` | `/api/tasks/:id/` | Update a task (partial) | ⬜ Coming in Section 6 |
| `DELETE` | `/api/tasks/:id/` | Delete a task | ⬜ Coming in Section 6 |

---

## Git Workflow

This project follows a **feature-branch workflow**. No code is committed directly to `main`.

```
main          ← production-ready code only; protected branch
  └── develop ← integration branch; all features merge here first
        └── feature/section-02-git-workflow   ← example feature branch
        └── feature/section-05-django-models
        └── feature/section-07-react-setup
```

**Standard workflow for each section:**

```bash
# 1. Make sure you're up to date
git checkout develop
git pull origin develop

# 2. Create a feature branch for the section
git checkout -b feature/section-XX-short-description

# 3. Do the work, then stage and commit
git add .
git commit -m "feat: descriptive commit message"

# 4. Push branch to GitHub
git push origin feature/section-XX-short-description

# 5. Open a Pull Request from feature branch → develop on GitHub
# 6. Review and merge the PR
# 7. Delete the feature branch after merge
```

**Commit message convention:**

| Prefix | When to use |
|---|---|
| `chore:` | Setup, config, tooling |
| `feat:` | New feature or functionality |
| `fix:` | Bug fix |
| `docs:` | README or documentation changes |
| `test:` | Adding or updating tests |
| `refactor:` | Code changes that don't add features or fix bugs |

---

## CI/CD Pipeline

> **Note:** The GitHub Actions pipeline will be documented here after Section 10.

The CI pipeline runs automatically on every pull request and includes:

- ⬜ Django unit tests (added in Section 10)
- ⬜ React ESLint check (added in Section 10)

---

## Contributing

This is a personal learning project. The workflow below mirrors how professional teams contribute to a shared codebase.

1. Branch off `develop` with a descriptive name: `feature/what-you-are-adding`
2. Write clear, focused commits using the commit convention above
3. Open a Pull Request into `develop` — never directly into `main`
4. The CI pipeline must pass before merging
5. Delete the feature branch after a successful merge

---

## License

This project is for educational purposes. No license applied.
