from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Dummy users DB (baad me DB connect hoga)
users_db = {
    "admin": {"password": "admin123", "credits": 100}
}

class CreditUpdate(BaseModel):
    username: str
    credits: int

@router.get("/users")
def list_users():
    return users_db

@router.post("/add-credits")
def add_credits(data: CreditUpdate):
    if data.username not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[data.username]["credits"] = users_db[data.username].get("credits", 0) + data.credits
    return {"message": f"Added {data.credits} credits to {data.username}"}
