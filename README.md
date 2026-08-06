# Link Manager — FastAPI Backend

A FastAPI backend for managing useful links found on the internet, classified by tags. It provides user management with role-based access control (`admin`, `user`).

This project is an API developed using Python, FastAPI, Clean Architecture, and design patterns (Strategy Pattern, Repository, Dependency Inversion).

## Features

- User management with role-based access (`admin`, `user`)
- Link management (CRUD) classified by tags
- JWT-based authentication, suitable for consumption by multiple frontends and mobile apps

## Stack

- **FastAPI** + **SQLAlchemy 2.0 (async)** + **Alembic**
- **PostgreSQL**, containerized via Docker (Rancher Desktop)
- **pytest** for testing, **CircleCI** + **Coveralls** planned for CI/coverage
