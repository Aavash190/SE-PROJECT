# Lab Project: Task Management API

A simple CRUD REST API for managing tasks, built with Django + Django REST Framework.

## Features
- Full CRUD (Create, Read, Update, Delete) on `Task` resources
- SQLite database (no setup needed)
- Auto-generated Swagger API docs
- Dockerized
- CI pipeline with linting, formatting checks, and test coverage

## Run locally
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
API available at `http://localhost:8000/api/tasks/`
Swagger docs at `http://localhost:8000/api/docs/`

## Run with Docker
```
docker compose up --build
```

## Run tests + coverage
```
python -m coverage run --source='tasks' manage.py test tasks
python -m coverage report -m
```
