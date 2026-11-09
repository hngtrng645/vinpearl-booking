import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [name, setName] = useState('');
  const [room, setRoom] = useState('Deluxe Ocean View');
  const [price, setPrice] = useState(4000000);
  const [message, setMessage] = useState('');
  const [bookings, setBookings] = useState([]);

  const API_GATEWAY = 'http://localhost:8000/api/booking';

  const fetchBookings = async () => {
    try {
      const res = await axios.get(API_GATEWAY);
      setBookings(res.data);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    fetchBookings();
  }, []);

  const handleBooking = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post(API_GATEWAY, {
        customer_name: name,
        room_type: room,
        base_price: price
      });
      setMessage(`Thành công! Mã đơn: ${res.data.booking_id} | Đã thanh toán: ${res.data.total_paid} VND`);
      fetchBookings();
    } catch (error) {
      setMessage('Lỗi khi đặt phòng!');
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1 style={{ color: '#003366' }}>Vinpearl Booking - SOA Architecture</h1>
      
      <form onSubmit={handleBooking} style={{ border: '1px solid #ccc', padding: '20px', width: '300px' }}>
        <h3>Đặt phòng mới</h3>
        <input type="text" placeholder="Tên khách hàng" required value={name} onChange={e => setName(e.target.value)} style={{width: '100%', marginBottom: '10px'}}/>
        <select value={room} onChange={e => setRoom(e.target.value)} style={{width: '100%', marginBottom: '10px'}}>
          <option value="Deluxe Ocean View">Deluxe Ocean View</option>
          <option value="Presidential Villa">Presidential Villa</option>
        </select>
        <input type="number" placeholder="Giá gốc" required value={price} onChange={e => setPrice(Number(e.target.value))} style={{width: '100%', marginBottom: '10px'}}/>
        <button type="submit" style={{width: '100%', padding: '10px', background: '#003366', color: 'white', border: 'none'}}>Xác nhận Đặt phòng</button>
      </form>

      {message && <p style={{ color: 'green', fontWeight: 'bold' }}>{message}</p>}

      <h3>Danh sách Đặt phòng (Từ Database SQLite)</h3>
      <table border="1" cellPadding="5" style={{borderCollapse: 'collapse'}}>
        <thead><tr><th>ID</th><th>Khách hàng</th><th>Hạng phòng</th><th>Tổng tiền (Đã tính thuế/phí)</th><th>Trạng thái</th></tr></thead>
        <tbody>
          {bookings.map(b => (
            <tr key={b.id}>
              <td>{b.id}</td><td>{b.customer_name}</td><td>{b.room_type}</td><td>{b.total_price} VND</td><td>{b.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;