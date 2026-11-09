from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import httpx
from database import SessionLocal, Booking

app = FastAPI(title="Vinpearl Booking Service (SOA)")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class BookingRequest(BaseModel):
    customer_name: str
    room_type: str
    base_price: float

@app.post("/api/v1/bookings")
async def create_booking(req: BookingRequest, db: Session = Depends(get_db)):
    # 1. Gọi Pricing Service (SOA Inter-service communication)
    async with httpx.AsyncClient() as client:
        try:
            price_response = await client.post(
                "http://pricing_service:8001/api/v1/calculate-price",
                json={"base_price": req.base_price, "discount_percent": 10.0} # Giả sử member 10%
            )
            price_data = price_response.json()
            final_price = price_data["total_amount"]
        except Exception as e:
            raise HTTPException(status_code=500, detail="Pricing Service Unavailable")

    # 2. Lưu vào CSDL (SQLite)
    new_booking = Booking(
        customer_name=req.customer_name, 
        room_type=req.room_type, 
        total_price=final_price
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    
    return {"message": "Booking successful", "booking_id": new_booking.id, "total_paid": final_price}

@app.get("/api/v1/bookings")
def get_bookings(db: Session = Depends(get_db)):
    return db.query(Booking).all()