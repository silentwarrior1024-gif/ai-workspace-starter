# FastAPI Backend

A backend service built with **FastAPI** for authentication, user management, AI tool orchestration, and database operations.

---

## 🚀 Features

- Authentication routes (`/login`, `/register`)  
- Admin endpoints (`/users`, `/audit`)  
- AI tool orchestration  
- Database models: `User`, `DataItem`, `Payment`, `AuditLog`  
- Ready for feature branch & PR workflow  

---

## 🛠 Prerequisites

- Python 3.10+  
- PostgreSQL (or your preferred DB)  
- pip (Python package manager)  
- Git  

---

## ⚡ Setup

1. **Clone the repo**
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
pip install -r requirements.txt
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your_secret_key
DEBUG=True
uvicorn main:app --reload
### Authentication
- `POST /register` → Create new user
- `POST /login` → Authenticate user
### Admin
- `GET /users` → List all users
- `POST /users` → Add new user
- `GET /audit` → Audit logs
### Orchestrator
- `POST /tools/run` → Run AI tools in parallel
git checkout -b feature/<feature-name>
curl -X POST http://127.0.0.1:8000/register \
-H "Content-Type: application/json" \
-d '{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "strongpassword123"
}'
curl -X POST http://127.0.0.1:8000/login \
-H "Content-Type: application/json" \
-d '{
  "username": "john_doe",
  "password": "strongpassword123"
}'
curl -X GET http://127.0.0.1:8000/users
curl -X POST http://127.0.0.1:8000/users \
-H "Content-Type: application/json" \
-d '{
  "username": "alice",
  "email": "alice@example.com",
  "password": "alicepassword"
}'
curl -X GET http://127.0.0.1:8000/audit
curl -X POST http://127.0.0.1:8000/tools/run \
-H "Content-Type: application/json" \
-d '{
  "tool_ids": [1, 2, 3],
  "input_data": "Sample input"
}'
uvicorn main:app --reload
git checkout -b feature/add-new-endpoint

