from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Vinpearl Pricing Service (SOA)")

class PriceRequest(BaseModel):
    base_price: float
    discount_percent: float = 0.0

@app.post("/api/v1/calculate-price")
def calculate_price(req: PriceRequest):
    # Rule BR-03: (Base - Discount) + 5% Service + 8% VAT
    discount_amount = req.base_price * (req.discount_percent / 100)
    price_after_discount = req.base_price - discount_amount
    service_charge = price_after_discount * 0.05
    vat = (price_after_discount + service_charge) * 0.08
    total = price_after_discount + service_charge + vat
    return {
        "base_price": req.base_price,
        "discount_applied": discount_amount,
        "service_charge": round(service_charge, 2),
        "vat": round(vat, 2),
        "total_amount": round(total, 2)
    }