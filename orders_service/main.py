from fastapi import FastAPI, HTTPException
import httpx
import os

app = FastAPI()

ORDERS = {
    1: [{"order_id": 101, "item": "Book"}],
    2: [{"order_id": 102, "item": "Pen"}],
}

USER_SERVICE_HOST = os.getenv("USER_SERVICE_HOST", "users_service")
USER_SERVICE_PORT = os.getenv("USER_SERVICE_PORT", "8001")


@app.get("/orders/{user_id}")
async def get_orders(user_id: int):
    # consult User Service to validate user exists
    url = f"http://{USER_SERVICE_HOST}:{USER_SERVICE_PORT}/users/{user_id}"
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(url, timeout=5.0)
    except httpx.RequestError:
        raise HTTPException(status_code=502, detail="Cannot reach User Service")

    if r.status_code == 404:
        raise HTTPException(status_code=404, detail="User not found")

    return ORDERS.get(user_id, [])
