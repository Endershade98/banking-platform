# Account Microservice

This microservice is responsible for managing bank accounts for users.  
It is designed following **Domain-Driven Design (DDD)** and **Clean Architecture** principles.

## Responsibilities

- Create new accounts
- Retrieve account information
- Get account balance
- Freeze accounts

> Note: Roles and permissions are managed by a separate microservice.

## Quickstart

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver