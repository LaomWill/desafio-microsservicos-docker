from fastapi import FastAPI, HTTPException

app = FastAPI()

USERS = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
]


@app.get("/users")
def get_users():
    return USERS


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for u in USERS:
        if u["id"] == user_id:
            return u
    raise HTTPException(status_code=404, detail="User not found")
