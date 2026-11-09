# Dự án Website Đặt phòng Vinpearl - Kiến trúc Hướng Dịch vụ (SOA) & Đảm bảo Chất lượng (SQA)

Dự án này được thiết kế để phục vụ 2 môn học:
1. **Phát triển phần mềm hướng dịch vụ (SOA):** Sử dụng kiến trúc Microservices với API Gateway và các dịch vụ độc lập (Booking, Pricing).
2. **Đảm bảo chất lượng phần mềm (SQA):** Tích hợp sẵn bộ test tự động (Pytest) tuân thủ tiêu chuẩn ISO/IEC 25010 (Độ chính xác tính toán, Test chịu tải cơ bản).

## 1. Cấu trúc thư mục
- `/backend`: Chứa các Microservices (FastAPI, Python).
  - `gateway.py`: API Gateway đóng vai trò điều phối.
  - `booking_service.py`: Dịch vụ quản lý đặt phòng, giao tiếp SQLite.
  - `pricing_service.py`: Dịch vụ tính toán giá (Thuế, Phí, Voucher).
  - `database.py`: Kết nối CSDL SQLite (SQLAlchemy).
- `/frontend`: Chứa giao diện người dùng (React, Vite).
- `/tests`: Chứa kịch bản kiểm thử tự động (Pytest).
- `docker-compose.yml`: File đóng gói toàn bộ dự án bằng Docker.

## 2. Hướng dẫn chạy dự án bằng Docker (Đóng gói)
Yêu cầu: Máy đã cài đặt Docker và Docker Compose.
```bash
docker-compose up --build
```
- Frontend: http://localhost:5173
- API Gateway: http://localhost:8000/docs (Giao diện Swagger UI)

## 3. Hướng dẫn đẩy code lên GitHub của bạn
Mở terminal tại thư mục giải nén dự án và chạy các lệnh sau:
```bash
git init
git add .
git commit -m "Khởi tạo dự án Vinpearl SOA & SQA"
git branch -M main
git remote add origin https://github.com/TENCUABAN/TEN_REPO_CUA_BAN.git
git push -u origin main
```

## 4. Chạy kịch bản Kiểm thử SQA (Pytest)
```bash
cd tests
pip install pytest requests
pytest test_sqa.py -v
```