from fastapi import FastAPI, HTTPException
import httpx
import os

app = FastAPI()

USERS_HOST = os.getenv("USERS_SERVICE_HOST", "users_service")
USERS_PORT = os.getenv("USERS_SERVICE_PORT", "8001")
ORDERS_HOST = os.getenv("ORDERS_SERVICE_HOST", "orders_service")
ORDERS_PORT = os.getenv("ORDERS_SERVICE_PORT", "8002")


@app.get("/api/users")
async def proxy_users():
    url = f"http://{USERS_HOST}:{USERS_PORT}/users"
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(url, timeout=10.0)
    except httpx.RequestError:
        raise HTTPException(status_code=502, detail="Cannot reach User Service")
    return r.json()


@app.get("/api/orders/{user_id}")
async def proxy_orders(user_id: int):
    url = f"http://{ORDERS_HOST}:{ORDERS_PORT}/orders/{user_id}"
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(url, timeout=10.0)
    except httpx.RequestError:
        raise HTTPException(status_code=502, detail="Cannot reach Order Service")

    if r.status_code == 404:
        raise HTTPException(status_code=404, detail="Not found")
    return r.json()
