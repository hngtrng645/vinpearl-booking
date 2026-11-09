import pytest
import requests

# Yêu cầu: Backend phải đang chạy (docker-compose up)

PRICING_URL = "http://localhost:8001/api/v1/calculate-price"

def test_tc_pric_01_iso25010_correctness():
    """
    Kiểm thử TC-PRIC-01: ISO/IEC 25010 Functional Correctness.
    Kiểm tra công thức tính giá BR-03.
    Đầu vào: Base = 4,000,000 | Giảm giá 10%
    Mong đợi: Tổng tiền = 4,082,400 (Theo công thức (4M - 10%) + 5% service + 8% VAT)
    """
    payload = {
        "base_price": 4000000.0,
        "discount_percent": 10.0
    }
    
    try:
        response = requests.post(PRICING_URL, json=payload)
        data = response.json()
        
        assert response.status_code == 200
        # 4,000,000 - 400,000 = 3,600,000
        # Service: 3,600,000 * 0.05 = 180,000
        # VAT: (3,600,000 + 180,000) * 0.08 = 302,400
        # Total: 3,600,000 + 180,000 + 302,400 = 4,082,400
        assert data["total_amount"] == 4082400.0, "Sai lệch thuật toán tính tổng tiền (Lỗi Mức S1)"
        print("PASS: Tính toán giá tiền chính xác tuyệt đối theo ISO 25010.")
    except requests.exceptions.ConnectionError:
        pytest.skip("Pricing Service chưa chạy, hãy dùng docker-compose up trước.")