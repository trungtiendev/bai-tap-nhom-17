# 🏨 Bài Tập Lớn Cấu Trúc Dữ Liệu & Giải Thuật

## Quản Lý Thuế Phòng Khách Sạn (C++)

---

## 📋 Thông Tin Chung

| Mục | Chi tiết |
|------|---------|
| **Trường** | Đại Học Mở Hà Nội |
| **Khoa** | Trung tâm Đào tạo E-learning |
| **Môn học** | Cấu trúc dữ liệu và giải thuật – IT05 |
| **Chủ đề** | **07** – Quản lý thuế phòng khách sạn |
| **Ngôn ngữ** | C++ (C++17) |
| **CTDL** | Danh sách liên kết đơn (Singly Linked List) |
| **Đối tượng** | Phòng khách sạn, Khách thuê phòng |

---

## 🎯 Mục Tiêu

Xây dựng chương trình quản lý thuế phòng khách sạn, cho phép:

- Quản lý thông tin **phòng khách sạn** và **khách hàng** đang thuê phòng
- Tính toán và thống kê **thuế phòng** tự động
- Lưu trữ dữ liệu bền vững qua **file văn bản**
- Tương tác qua **giao diện menu** trực quan

---

## 🧠 Kiến Thức Áp Dụng

- **Danh sách liên kết đơn** (Singly Linked List)
- **Lập trình hướng đối tượng** (Class, Template, Encapsulation)
- **Các thuật toán:** Thêm, Xóa, Sửa, Tìm kiếm, Sắp xếp, Thống kê
- **Xử lý file** (Đọc/Ghi text file)
- **Xử lý ngoại lệ** (try-catch)
- **Xử lý chuỗi** (stringstream, nhập liệu an toàn)

---

## 📂 Cấu Trúc Thư Mục

```
ctdl/
├── quanlykhachsan.cpp          # Mã nguồn chính (C++)
├── quanlykhachsan_cpp          # Binary đã biên dịch
├── rooms.txt                    # Dữ liệu phòng (tự động tạo)
├── guests.txt                   # Dữ liệu khách (tự động tạo)
├── phan-tich.md                 # Tài liệu phân tích thiết kế
├── Bao_cao_CTDL_Chu_de_07.docx  # Báo cáo Word (C)
├── Bao_cao_CTDL_Chu_de_07_CPP.docx  # Báo cáo Word (C++)
├── create_report.py             # Script tạo báo cáo (C)
├── create_report_cpp.py         # Script tạo báo cáo (C++)
└── README.md                    # Hướng dẫn sử dụng
```

---

## 🔧 Yêu Cầu Hệ Thống

| Thành phần | Yêu cầu |
|-----------|---------|
| **Hệ điều hành** | Windows / Linux / macOS |
| **Trình biên dịch** | g++ (hỗ trợ C++17) hoặc tương đương |
| **Dung lượng** | Tối thiểu 10 MB trống |

### Kiểm tra trình biên dịch

```bash
g++ --version
# Output mẫu: g++ (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
```

---

## 🚀 Hướng Dẫn Cài Đặt & Chạy

### 1. Biên dịch chương trình

```bash
cd /đường/dẫn/đến/thư/mục/ctdl

# Biên dịch với C++17
g++ -std=c++17 -o quanlykhachsan_cpp quanlykhachsan.cpp

# Nếu không có lỗi, sẽ tạo file thực thi quanlykhachsan_cpp
```

### 2. Chạy chương trình

```bash
# Linux / macOS
./quanlykhachsan_cpp

# Windows
quanlykhachsan_cpp.exe
```

### 3. Sử dụng

Chương trình khởi động với menu chính:

```
+====================== QUAN LY THUE PHONG KHACH SAN ======================+
| 1. Quan ly Phong          2. Quan ly Khach          3. Sap xep           |
| 4. Tim Max/Min            5. Thong ke               6. Luu file          |
| 7. Doc file               0. Thoat                                        |
+===========================================================================+
Chon:
```

> **Mẹo:** Nhập số tương ứng và nhấn Enter để chọn chức năng.

---

## 📖 Danh Sách Chức Năng

### 1. Quản lý Phòng

| Mã | Chức năng | Mô tả |
|:--:|-----------|-------|
| 1.1 | **Thêm phòng** | Nhập thông tin phòng mới. Tự động kiểm tra trùng mã. |
| 1.2 | **Hiển thị** | In danh sách tất cả phòng dưới dạng bảng. |
| 1.3 | **Tìm theo mã** | Tra cứu phòng bằng mã phòng. |
| 1.4 | **Tìm theo loại** | Liệt kê phòng theo loại (Đơn/Đôi/VIP). |
| 1.5 | **Sửa** | Cập nhật thông tin phòng. |
| 1.6 | **Xóa** | Xóa phòng (chỉ xóa được khi không có khách đang thuê). |

### 2. Quản lý Khách

| Mã | Chức năng | Mô tả |
|:--:|-----------|-------|
| 2.1 | **Thêm khách** | Nhập thông tin khách. Tự động chuẩn hóa tên, cập nhật trạng thái phòng. |
| 2.2 | **Hiển thị** | In danh sách tất cả khách dưới dạng bảng. |
| 2.3 | **Tìm theo CMND** | Tra cứu khách bằng số CMND/CCCD. |
| 2.4 | **Tìm theo tên** | Tra cứu khách theo tên (tìm gần đúng). |
| 2.5 | **Sửa** | Cập nhật thông tin khách. |
| 2.6 | **Xóa** | Xóa khách và tự động cập nhật trạng thái phòng về "Trống". |

### 3. Sắp xếp

| Mã | Chức năng | Thuật toán |
|:--:|-----------|:----------:|
| 3.1 | Phòng theo giá **tăng dần** | Bubble Sort |
| 3.2 | Phòng theo giá **giảm dần** | Bubble Sort |
| 3.3 | Phòng theo **mã phòng** | Bubble Sort |
| 3.4 | Khách theo **tên A-Z** | Bubble Sort |

### 4. Tìm Max / Min

| Mã | Chức năng |
|:--:|-----------|
| 4.1 | Phòng có giá thuê **cao nhất** |
| 4.2 | Phòng có giá thuê **thấp nhất** |
| 4.3 | Khách ở **lâu nhất** (nhiều đêm nhất) |
| 4.4 | Khách **mới nhất** (gần đây nhất) |

### 5. Thống kê

Chương trình thống kê tự động 7 chỉ tiêu:

| STT | Chỉ tiêu | Đơn vị |
|:---:|----------|:------:|
| 1 | Tổng số phòng | phòng |
| 2 | Phòng đang thuê | phòng |
| 3 | Phòng trống | phòng |
| 4 | Phòng loại Đơn | phòng |
| 5 | Phòng loại Đôi | phòng |
| 6 | Phòng loại VIP | phòng |
| 7 | Tổng số khách | khách |
| 8 | Tổng doanh thu thuế | VNĐ |

### 6. Lưu / Đọc File

| Mã | Chức năng | File |
|:--:|-----------|:----:|
| 6 | **Lưu file** | `rooms.txt`, `guests.txt` |
| 7 | **Đọc file** | `rooms.txt`, `guests.txt` |

> **Tự động:** Chương trình tự động đọc file khi khởi động và tự động lưu khi thoát.

---

## 🧱 Kiến Trúc Chương Trình

```
┌─────────────────────────────────────────────────────────────┐
│                    HotelManager (class)                     │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐    ┌──────────────┐                       │
│  │ LinkedList  │    │  LinkedList  │                       │
│  │   <Room>    │    │   <Guest>    │                       │
│  └──────┬──────┘    └──────┬───────┘                       │
│         │                  │                                │
│  ┌──────▼──────┐    ┌──────▼───────┐                       │
│  │ Node<Room>  │    │ Node<Guest>  │                       │
│  │ ├ Room data │    │ ├ Guest data │                       │
│  │ └ Node* next│    │ └ Node* next │                       │
│  └─────────────┘    └──────────────┘                       │
│                                                             │
│  Phuong thuc: them, sua, xoa, tim, sap xep, thong ke       │
│  Xu ly file: docFileTuDong(), ghiFileTuDong()              │
└─────────────────────────────────────────────────────────────┘
```

### Các lớp chính

```cpp
class Room       // Phòng khách sạn: mã, loại, giá thuê, trạng thái, thuế suất
class Guest      // Khách thuê phòng: mã, họ tên, CMND, mã phòng, số đêm, ngày đến
template<T>
class Node       // Nút DSLK đơn: data (T), next (Node<T>*)
template<T>
class LinkedList // DSLK đơn: head, count, các thao tác thêm/xóa/tìm/sắp xếp
class HotelManager // Lớp quản lý chính: 2 DSLK, menu, file I/O
```

---

## 📊 Bộ Dữ Liệu Mẫu

### Phòng

| Mã phòng | Loại | Giá thuê | Trạng thái | Thuế suất |
|:--------:|:----:|:--------:|:----------:|:---------:|
| P001 | Đơn | 500,000 VND | Có khách | 5% |
| P002 | Đôi | 800,000 VND | Có khách | 8% |
| P003 | VIP | 2,000,000 VND | Trống | 10% |
| P004 | Đôi | 750,000 VND | Trống | 5% |
| P005 | Đơn | 450,000 VND | Có khách | 5% |

### Khách

| Mã khách | Họ tên | CMND | Mã phòng | Số đêm | Ngày đến |
|:--------:|:------:|:----:|:--------:|:------:|:--------:|
| K001 | Nguyễn Văn A | 123456789 | P001 | 3 | 01/03/2025 |
| K002 | Trần Thị B | 987654321 | P002 | 5 | 28/02/2025 |
| K003 | Lê Văn C | 456789123 | P005 | 2 | 05/03/2025 |

---

## ⚙️ Xử Lý Lỗi

Chương trình xử lý các tình huống lỗi sau:

| Tình huống | Xử lý |
|------------|-------|
| Nhập mã phòng/khách trùng | Thông báo lỗi, yêu cầu nhập lại |
| Nhập sai kiểu dữ liệu (chữ vào chỗ số) | Vòng lặp kiểm tra + thông báo |
| Giá thuê ≤ 0 | Yêu cầu nhập số dương |
| Số đêm ngoài phạm vi 1-365 | Kiểm tra biên |
| Mã phòng không tồn tại khi thêm khách | Chặn thêm, thông báo lỗi |
| Xóa phòng đang có khách thuê | Chặn xóa, thông báo lý do |
| File không tồn tại | Tạo danh sách rỗng, không báo lỗi |

---

## 🛠 Biên Dịch & Debug

### Các tùy chọn biên dịch

```bash
# Debug mode (có thông tin gỡ lỗi)
g++ -std=c++17 -g -o quanlykhachsan_cpp quanlykhachsan.cpp

# Optimization mode
g++ -std=c++17 -O2 -o quanlykhachsan_cpp quanlykhachsan.cpp

// Full warnings
g++ -std=c++17 -Wall -Wextra -o quanlykhachsan_cpp quanlykhachsan.cpp
```

### Chạy với valgrind (kiểm tra rò rỉ bộ nhớ - Linux)

```bash
valgrind --leak-check=full ./quanlykhachsan_cpp
```

---

## 📝 Ghi Chú

- Dữ liệu được lưu ở định dạng **text** (`rooms.txt`, `guests.txt`) — có thể mở và chỉnh sửa bằng bất kỳ trình soạn thảo nào
- Mỗi dòng trong file lưu 1 bản ghi, các trường cách nhau bằng dấu `|`
- Chương trình tự động **chuẩn hóa tên khách** (viết hoa chữ cái đầu mỗi từ)
- Khi **xóa khách**, trạng thái phòng tự động chuyển về "Trống"
- Khi **thêm khách**, trạng thái phòng tự động chuyển về "Có khách"
- Không thể xóa phòng đang có khách thuê

---

## 📞 Liên Hệ

**Giảng viên hướng dẫn:** …

**Sinh viên thực hiện:** …

---

## 📄 Giấy Phép

Bài tập lớn này được thực hiện với mục đích học tập tại Đại Học Mở Hà Nội.

---

*Hà Nội – 2025*
