# Kiểm tra vấn đáp — Cấu trúc dữ liệu & Giải thuật (IT05)

## Thông tin buổi thi

- **Hình thức:** Vấn đáp trực tuyến
- **Môn:** Cấu trúc dữ liệu và giải thuật – IT05
- **Chủ đề:** 07 – Quản lý thuế phòng khách sạn
- **CTDL:** Danh sách liên kết đơn (Singly Linked List)
- **Ngôn ngữ:** C++17

## Câu hỏi

### Câu 1: BTL sử dụng cấu trúc dữ liệu gì để lưu trữ? Đối tượng được quản lý chính là gì?

**Trả lời:**
- **CTDL:** Danh sách liên kết đơn (Singly Linked List) – mỗi phần tử là `Node<T>` gồm `data` và con trỏ `next`
- **Đối tượng:**
  - `Room` (Phòng khách sạn): `maPhong`, `loaiPhong`, `giaThue`, `tinhTrang`, `thueSuat`
  - `Guest` (Khách thuê phòng): `maKhach`, `hoTen`, `cmnd`, `maPhongThue`, `soDem`, `ngayDen`

### Câu 2: BTL đã thực hiện được những yêu cầu xử lý gì?

**Trả lời:** 7 nhóm chức năng:
1. **Quản lý Phòng:** Thêm, Hiển thị, Tìm theo mã, Tìm theo loại, Sửa, Xóa
2. **Quản lý Khách:** Thêm, Hiển thị, Tìm theo CMND, Tìm theo tên, Sửa, Xóa
3. **Sắp xếp:** Bubble Sort – phòng theo giá, mã; khách theo tên
4. **Tìm Max/Min:** Phòng giá cao/thấp nhất, khách ở lâu/mới nhất
5. **Thống kê:** 8 chỉ tiêu (số phòng, trạng thái, loại, tổng khách, doanh thu thuế)
6. **File I/O:** Tự động đọc/ghi file text
7. **Xử lý ngoại lệ:** Kiểm tra kiểu, ràng buộc nghiệp vụ, try-catch

### Câu 3: Viết yêu cầu xử lý mới — In phần tử thứ k từ đầu danh sách

**Yêu cầu:** In thông tin phần tử thứ k (1 ≤ k ≤ n) từ đầu DSLK, với k nhập từ bàn phím.

**Cài đặt:** Thêm chức năng `inPhongThuK()` và `inKhachThuK()` trong `HotelManager`:
- Dùng `getHead()` + duyệt tuần tự đến vị trí k
- Kiểm tra k hợp lệ qua `nhapInt(..., 1, rooms.size())`
- Độ phức tạp: O(k), trường hợp xấu nhất O(n)

**Bổ sung menu:**
- Menu Phòng: `7.In phong thu k`
- Menu Khách: `7.In khach thu k`

## Ghi chú

- Code đã biên dịch thành công với `g++ -std=c++17`
- Hoàn toàn sử dụng DSLK đơn, không dùng mảng hay vector
- Các kiến thức RAG Brain có sẵn: 8 bài giảng CTDL&GT của Đại Học Mở Hà Nội
