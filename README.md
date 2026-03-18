# HRMS Backend

A lightweight HRMS Lite backend built with FastAPI and MongoDB.

## Features

- Employee management
  - Add employee
  - List employees
  - Delete employee
- Attendance management
  - Mark attendance
  - View all attendance
  - View attendance by employee
- Dashboard summary
- Validation and proper error handling
- Logging middleware
- MongoDB indexes for uniqueness

## Tech Stack

- FastAPI
- PyMongo
- MongoDB
- Pydantic

## Setup

1. Create virtual environment

```bash
python -m venv .venv
```

2. Activate virtual environment

```bash
.venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create .env
   Copy .env.example to .env and update values.

5. Run the server

```bash
uvicorn app.main:app --reload
```

7. API Docs availble - http://127.0.0.1:8000/docs
