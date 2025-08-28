from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Fake DB for demo (baad me real DB se connect hoga)
users_db = {}

class User(BaseModel):
    username: str
    password: str

@router.post("/signup")
def signup(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.username] = user.password
    return {"message": "User created successfully"}

@router.post("/login")
def login(user: User):
    if user.username not in users_db or users_db[user.username] != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": f"Welcome {user.username}!"}
