from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI(title="Vinpearl API Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BOOKING_URL = "http://booking_service:8002"

@app.post("/api/booking")
async def route_booking(request: Request):
    data = await request.json()
    async with httpx.AsyncClient() as client:
        res = await client.post(f"{BOOKING_URL}/api/v1/bookings", json=data)
        return res.json()

@app.get("/api/booking")
async def get_bookings():
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{BOOKING_URL}/api/v1/bookings")
        return res.json()