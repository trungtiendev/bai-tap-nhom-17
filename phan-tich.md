# PHÂN TÍCH THIẾT KẾ BÀI TOÁN
## Quản lý thuế phòng khách sạn
### Môn: Cấu trúc dữ liệu và giải thuật – IT05

---

## 1. XÁC ĐỊNH BÀI TOÁN

### 1.1. Mô tả bài toán
Xây dựng chương trình quản lý thuế phòng khách sạn. Hệ thống cho phép quản lý thông tin các phòng khách sạn và khách hàng đang thuê phòng, từ đó tính toán và thống kê thuế phòng. Chương trình hỗ trợ nhập xuất dữ liệu bằng tay hoặc thông qua file để đảm bảo dữ liệu được lưu trữ bền vững.

### 1.2. Yêu cầu chi tiết

| STT | Nhóm chức năng | Yêu cầu tối thiểu | Điểm |
|:---:|----------------|:-----------------:|:----:|
| 1 | Nhập/In danh sách, Đọc/Ghi file | 1 bộ nhập-in + đọc-ghi file | 2.0 |
| 2 | Tìm, sửa, xóa đối tượng | - | 1.5 |
| 3 | Tìm kiếm đối tượng | 2 yêu cầu | 0.5 |
| 4 | Sắp xếp đối tượng | 4 yêu cầu | 2.0 |
| 5 | Tìm lớn nhất / nhỏ nhất | 4 yêu cầu | 1.0 |
| 6 | Thống kê | 5 yêu cầu | 1.0 |
| 7 | Lưu trữ chức năng (tổ chức menu) | - | 1.0 |
| **Tổng** | | | **10.0** |

### 1.3. Đối tượng quản lý
Chương trình quản lý **02 đối tượng chính**:
1. **Phòng khách sạn (Room)** – các phòng có sẵn trong khách sạn
2. **Khách thuê phòng (Guest)** – khách hàng đang thuê phòng

---

## 2. XÁC ĐỊNH CTDL BIỂU DIỄN BÀI TOÁN

### 2.1. Lựa chọn CTDL: **Danh sách liên kết đơn (Singly Linked List)**

**Lý do chọn:**
- Số lượng phòng và khách thay đổi linh hoạt (thêm/xóa thường xuyên) → DSLK đơn không cần cấp phát tĩnh trước
- Thao tác duyệt tuần tự phù hợp với các yêu cầu in danh sách, tìm kiếm, thống kê
- Bộ nhớ chỉ dùng đúng bằng số phần tử thực tế
- Cài đặt đơn giản, dễ hiểu, phù hợp mức độ sinh viên

### 2.2. Thông tin quản lý của từng đối tượng

#### Đối tượng 1: Phòng khách sạn (Room)

| Trường | Kiểu dữ liệu | Mô tả |
|--------|:-----------:|-------|
| maPhong | char[10] | Mã phòng (vd: P001, P002) |
| soPhong | int | Số phòng (vd: 101, 202) |
| tang | int | Tầng (vd: 1, 2, 3) |
| loaiPhong | char[20] | Loại phòng (Đơn, Đôi, VIP, Suite) |
| giaThue | float | Giá thuê phòng (VNĐ/đêm) |
| trangThai | int | Trạng thái (0 = Trống, 1 = Đã đặt, 2 = Đang thuê) |

#### Đối tượng 2: Khách thuê phòng (Guest)

| Trường | Kiểu dữ liệu | Mô tả |
|--------|:-----------:|-------|
| maKhach | char[10] | Mã khách (vd: K001, K002) |
| hoTen | char[50] | Họ tên khách hàng |
| cmnd | char[12] | Số CMND/CCCD |
| sdt | char[15] | Số điện thoại |
| maPhong | char[10] | Mã phòng đang thuê (liên kết với Room) |
| ngayNhan | char[10] | Ngày nhận phòng (dd/mm/yyyy) |
| ngayTra | char[10] | Ngày trả phòng dự kiến (dd/mm/yyyy) |
| soDem | int | Số đêm ở (tự động tính) |
| tienPhong | float | Tiền phòng = giaThue × soDem |
| thue | float | Thuế phòng = 10% × tienPhong |

### 2.3. Định nghĩa cấu trúc dữ liệu (dạng mã giả C)

```c
// -------------------------------------------------------
// 1. CẤU TRÚC PHÒNG KHÁCH SẠN
// -------------------------------------------------------
struct Room {
    char maPhong[10];      // Mã phòng
    int soPhong;           // Số phòng
    int tang;              // Tầng
    char loaiPhong[20];    // Loại phòng
    float giaThue;         // Giá thuê (VNĐ/đêm)
    int trangThai;         // 0=Trống, 1=Đã đặt, 2=Đang thuê
};

// -------------------------------------------------------
// 2. CẤU TRÚC KHÁCH THUÊ PHÒNG
// -------------------------------------------------------
struct Guest {
    char maKhach[10];      // Mã khách
    char hoTen[50];        // Họ tên
    char cmnd[12];         // CMND/CCCD
    char sdt[15];          // Số điện thoại
    char maPhong[10];      // Mã phòng đang thuê
    char ngayNhan[10];     // Ngày nhận phòng
    char ngayTra[10];      // Ngày trả phòng dự kiến
    int soDem;             // Số đêm ở
    float tienPhong;       // Tiền phòng = giaThue * soDem
    float thue;            // Thuế phòng = 10% * tienPhong
};

// -------------------------------------------------------
// 3. NÚT CỦA DSLK ĐƠN (dùng chung cho cả 2 danh sách)
// -------------------------------------------------------
struct Node {
    void *data;            // Con trỏ tới dữ liệu (Room* hoặc Guest*)
    struct Node *next;     // Con trỏ tới nút kế tiếp
};

// -------------------------------------------------------
// 4. DANH SÁCH LIÊN KẾT ĐƠN
// -------------------------------------------------------
struct LinkedList {
    Node *head;            // Con trỏ đầu danh sách
    Node *tail;            // Con trỏ cuối danh sách
    int size;              // Số lượng phần tử
};
```

### 2.4. Input và Output của bài toán

**Input:**
- Nhập từ bàn phím: thông tin phòng, thông tin khách
- Đọc từ file văn bản: `rooms.txt` (danh sách phòng), `guests.txt` (danh sách khách)

**Output:**
- In ra màn hình: danh sách phòng, danh sách khách, kết quả tìm kiếm, sắp xếp, thống kê
- Ghi ra file: `rooms.txt`, `guests.txt`
- Màn hình menu tương tác với người dùng

---

## 3. XÁC ĐỊNH CÁC THUẬT TOÁN

### 3.1. Các hàm xử lý danh sách (nền tảng)

| STT | Hàm | Mô tả |
|:---:|-----|-------|
| 1 | `initList(L)` | Khởi tạo danh sách rỗng |
| 2 | `addHead(L, data)` | Thêm nút vào đầu danh sách |
| 3 | `addTail(L, data)` | Thêm nút vào cuối danh sách |
| 4 | `deleteNode(L, key)` | Xóa nút theo mã (maPhong / maKhach) |
| 5 | `searchNode(L, key)` | Tìm nút theo mã, trả về con trỏ nút |
| 6 | `freeList(L)` | Giải phóng toàn bộ danh sách |

### 3.2. Các chức năng với đối tượng Phòng (Room)

#### Nhập – In – Đọc/Ghi file (2 điểm)

| STT | Chức năng | Mô tả |
|:---:|-----------|-------|
| 1 | `nhapPhong()` | Nhập thông tin một phòng từ bàn phím. Kiểm tra mã phòng không trùng, giá thuê > 0, các trường không rỗng. |
| 2 | `nhapDSPhong(L_Phong)` | Nhập danh sách phòng (gọi `nhapPhong()` nhiều lần theo số lượng) |
| 3 | `inDSPhong(L_Phong)` | In danh sách phòng ra màn hình dưới dạng bảng |
| 4 | `docFilePhong(L_Phong, filename)` | Đọc danh sách phòng từ file `rooms.txt` |
| 5 | `ghiFilePhong(L_Phong, filename)` | Ghi danh sách phòng vào file `rooms.txt` |

#### Tìm – Sửa – Xóa (1.5 điểm)

| STT | Chức năng | Mô tả |
|:---:|-----------|-------|
| 6 | `suaPhong(L_Phong, maPhong)` | Sửa thông tin phòng theo mã: tìm phòng, hiển thị thông tin cũ, nhập thông tin mới, cập nhật |
| 7 | `xoaPhong(L_Phong, maPhong)` | Xóa phòng theo mã: tìm và xóa nút khỏi DSLK |

#### Tìm kiếm (0.5 điểm – tối thiểu 2)

| STT | Chức năng | Mô tả |
|:---:|-----------|-------|
| 8 | `timPhongTheoMa(L_Phong, maPhong)` | Tìm phòng theo mã phòng. Duyệt DSLK, so sánh mã. |
| 9 | `timPhongTheoLoai(L_Phong, loaiPhong)` | Tìm tất cả phòng theo loại (Đơn/Đôi/VIP). Duyệt toàn bộ danh sách. |

#### Sắp xếp (2 điểm – tối thiểu 4 yêu cầu)

| STT | Chức năng | Ý nghĩa |
|:---:|-----------|---------|
| 10 | `sapXepPhongTheoGiaTang(L_Phong)` | Sắp xếp phòng theo giá thuê tăng dần (giá rẻ → đắt) |
| 11 | `sapXepPhongTheoGiaGiam(L_Phong)` | Sắp xếp phòng theo giá thuê giảm dần (giá đắt → rẻ) |
| 12 | `sapXepPhongTheoSoPhongTang(L_Phong)` | Sắp xếp phòng theo số phòng tăng dần |
| 13 | `sapXepPhongTheoTangVaSoPhong(L_Phong)` | Sắp xếp phòng theo tầng (tăng), cùng tầng thì theo số phòng (tăng) |

> **Thuật toán sắp xếp**: Sử dụng **Interchange Sort** hoặc **Selection Sort** trên DSLK đơn (đổi dữ liệu giữa các nút, không đổi liên kết).

#### Tìm lớn nhất / nhỏ nhất (1 điểm – tối thiểu 4 yêu cầu)

| STT | Chức năng | Mô tả |
|:---:|-----------|-------|
| 14 | `phongGiaThueCaoNhat(L_Phong)` | Tìm phòng có giá thuê cao nhất |
| 15 | `phongGiaThueThapNhat(L_Phong)` | Tìm phòng có giá thuê thấp nhất |
| 16 | `phongDangThueGiaCaoNhat(L_Phong)` | Tìm phòng đang được thuê có giá cao nhất |
| 17 | `phongTrongGiaThapNhat(L_Phong)` | Tìm phòng trống có giá thuê thấp nhất |

### 3.3. Các chức năng với đối tượng Khách (Guest)

#### Nhập – In – Đọc/Ghi file (2 điểm – chung với Phòng)

| STT | Chức năng | Mô tả |
|:---:|-----------|-------|
| 18 | `nhapKhach(L_Phong, L_Khach)` | Nhập thông tin khách. Tự động kiểm tra mã phòng có tồn tại trong danh sách phòng không, tính `soDem`, `tienPhong` = `giaThue × soDem`, `thue` = 10% × `tienPhong` |
| 19 | `nhapDSKhach(L_Phong, L_Khach)` | Nhập danh sách khách |
| 20 | `inDSKhach(L_Khach)` | In danh sách khách ra màn hình |
| 21 | `docFileKhach(L_Phong, L_Khach, filename)` | Đọc danh sách khách từ file `guests.txt` |
| 22 | `ghiFileKhach(L_Khach, filename)` | Ghi danh sách khách vào file `guests.txt` |

#### Tìm – Sửa – Xóa (1.5 điểm – chung với Phòng)

| STT | Chức năng | Mô tả |
|:---:|-----------|-------|
| 23 | `suaKhach(L_Phong, L_Khach, maKhach)` | Sửa thông tin khách theo mã. Cập nhật lại `tienPhong` và `thue`. |
| 24 | `xoaKhach(L_Phong, L_Khach, maKhach)` | Xóa khách theo mã. Cập nhật trạng thái phòng về 0 (Trống). |

#### Tìm kiếm (0.5 điểm – tối thiểu 2 yêu cầu)

| STT | Chức năng | Mô tả |
|:---:|-----------|-------|
| 25 | `timKhachTheoCMND(L_Khach, cmnd)` | Tìm khách theo số CMND |
| 26 | `timKhachTheoTen(L_Khach, hoTen)` | Tìm khách theo họ tên (gần đúng, chứa chuỗi) |

#### Sắp xếp (2 điểm – tối thiểu 4 yêu cầu)

| STT | Chức năng | Mô tả |
|:---:|-----------|-------|
| 27 | `sapXepKhachTheoTenTang(L_Khach)` | Sắp xếp khách theo tên (A → Z) |
| 28 | `sapXepKhachTheoTenGiam(L_Khach)` | Sắp xếp khách theo tên (Z → A) |
| 29 | `sapXepKhachTheoSoDemGiam(L_Khach)` | Sắp xếp khách theo số đêm ở giảm dần (ở lâu nhất → mới nhất) |
| 30 | `sapXepKhachTheoThueGiam(L_Khach)` | Sắp xếp khách theo tiền thuế phải đóng giảm dần |

#### Tìm lớn nhất / nhỏ nhất (1 điểm – tối thiểu 4 yêu cầu)

| STT | Chức năng | Mô tả |
|:---:|-----------|-------|
| 31 | `khachOLauNhat(L_Khach)` | Tìm khách có số đêm ở nhiều nhất |
| 32 | `khachMoiNhat(L_Khach)` | Tìm khách có số đêm ở ít nhất |
| 33 | `khachDongThueCaoNhat(L_Khach)` | Tìm khách đóng thuế phòng nhiều nhất |
| 34 | `khachDongThueThapNhat(L_Khach)` | Tìm khách đóng thuế phòng ít nhất |

### 3.4. Thống kê (1 điểm – tối thiểu 5 yêu cầu)

| STT | Chức năng | Mô tả |
|:---:|-----------|-------|
| 35 | `thongKeTongSoPhong(L_Phong)` | Đếm tổng số phòng trong khách sạn |
| 36 | `thongKeTongSoKhach(L_Khach)` | Đếm tổng số khách đang thuê |
| 37 | `thongKeSoPhongDangThue(L_Phong)` | Đếm số phòng đang có khách thuê (trangThai == 2) |
| 38 | `thongKeSoPhongTrong(L_Phong)` | Đếm số phòng trống (trangThai == 0) |
| 39 | `thongKeTongDoanhThuThue(L_Khach)` | Tính tổng thuế phòng thu được từ tất cả khách |
| 40 | `thongKePhongTheoTang(L_Phong, tang)` | Thống kê số phòng theo từng tầng |
| 41 | `thongKeKhachTheoPhong(L_Khach, maPhong)` | Liệt kê tất cả khách đang ở một phòng cụ thể |

### 3.5. Tổ chức menu chương trình (1 điểm)

```
=========================================================================
          CHƯƠNG TRÌNH QUẢN LÝ THUẾ PHÒNG KHÁCH SẠN
=========================================================================
0. Thoát chương trình
1. Nhập dữ liệu
   1.1. Nhập danh sách phòng
   1.2. Nhập danh sách khách
2. In danh sách
   2.1. In danh sách phòng
   2.2. In danh sách khách
3. Đọc/Ghi file
   3.1. Đọc dữ liệu từ file
   3.2. Ghi dữ liệu ra file
4. Tìm, sửa, xóa
   4.1. Sửa thông tin phòng
   4.2. Sửa thông tin khách
   4.3. Xóa phòng
   4.4. Xóa khách
5. Tìm kiếm
   5.1. Tìm phòng theo mã
   5.2. Tìm phòng theo loại
   5.3. Tìm khách theo CMND
   5.4. Tìm khách theo tên
6. Sắp xếp
   6.1. Sắp xếp phòng theo giá tăng dần
   6.2. Sắp xếp phòng theo giá giảm dần
   6.3. Sắp xếp phòng theo số phòng tăng dần
   6.4. Sắp xếp phòng theo tầng và số phòng
   6.5. Sắp xếp khách theo tên A→Z
   6.6. Sắp xếp khách theo tên Z→A
   6.7. Sắp xếp khách theo số đêm giảm dần
   6.8. Sắp xếp khách theo thuế giảm dần
7. Tìm lớn nhất / nhỏ nhất
   7.1. Phòng có giá thuê cao nhất
   7.2. Phòng có giá thuê thấp nhất
   7.3. Phòng đang thuê có giá cao nhất
   7.4. Phòng trống có giá thấp nhất
   7.5. Khách ở lâu nhất
   7.6. Khách ở ít nhất (mới nhất)
   7.7. Khách đóng thuế nhiều nhất
   7.8. Khách đóng thuế ít nhất
8. Thống kê
   8.1. Tổng số phòng
   8.2. Tổng số khách
   8.3. Số phòng đang thuê
   8.4. Số phòng trống
   8.5. Tổng doanh thu thuế
   8.6. Thống kê phòng theo tầng
   8.7. Thống kê khách theo phòng
=========================================================================
Mời bạn chọn chức năng (0-8):
```

### 3.6. Xử lý lỗi nhập liệu

| STT | Tình huống | Xử lý |
|:---:|------------|-------|
| 1 | Nhập mã phòng trùng | Yêu cầu nhập lại mã khác |
| 2 | Nhập mã khách trùng | Yêu cầu nhập lại mã khác |
| 3 | Giá thuê ≤ 0 | Yêu cầu nhập lại, giá thuê > 0 |
| 4 | Số đêm ≤ 0 | Kiểm tra ngày nhập/trả, đảm bảo soDem >= 1 |
| 5 | Mã phòng không tồn tại khi thêm khách | Thông báo lỗi, yêu cầu nhập lại |
| 6 | Nhập sai kiểu dữ liệu (chữ vào số) | Dùng fflush(stdin) + vòng lặp kiểm tra |
| 7 | File không tồn tại khi đọc | Thông báo lỗi, tạo danh sách rỗng |
| 8 | Nhập số tầng không hợp lệ | Chỉ chấp nhận 1 ≤ tang ≤ 10 |

### 3.7. Định dạng file lưu trữ

**File `rooms.txt`** (dòng đầu là số lượng phòng, mỗi dòng sau là 1 phòng):

```
<soLuongPhong>
<maPhong>|<soPhong>|<tang>|<loaiPhong>|<giaThue>|<trangThai>
...
```

**File `guests.txt`** (dòng đầu là số lượng khách, mỗi dòng sau là 1 khách):

```
<soLuongKhach>
<maKhach>|<hoTen>|<cmnd>|<sdt>|<maPhong>|<ngayNhan>|<ngayTra>|<soDem>|<tienPhong>|<thue>
...
```

### 3.8. Lưu đồ tổng quát chương trình

```
           BẮT ĐẦU
              │
              ▼
    Khởi tạo 2 DSLK rỗng (L_Phong, L_Khach)
              │
              ▼
    Đọc dữ liệu từ file (nếu có)
              │
              ▼
   ┌─────────────────────────┐
   │   HIỂN THỊ MENU CHÍNH   │
   │   Người dùng chọn số     │
   └─────────┬───────────────┘
             │
             ▼
    ┌──────────────────────┐
    │ Phân luồng chức năng │
    │ theo số người dùng   │
    │ chọn                │
    └─────────┬────────────┘
             │
     ┌───────┴───────┐
     │               │
   Chức năng      Thoát
   tương ứng      (0)
     │               │
     ▼               ▼
  Quay lại       KẾT THÚC
  menu         Ghi file tự động
```

---

## 4. MA TRẬN YÊU CẦU – CHỨC NĂNG

| Yêu cầu | Số lượng | Các chức năng tương ứng |
|---------|:--------:|-------------------------|
| Nhập – In – File | 2 điểm | #1–5 (Phòng), #18–22 (Khách) |
| Tìm, sửa, xóa | 1.5 điểm | #6–7 (Phòng), #23–24 (Khách) |
| Tìm kiếm (≥ 2) | 0.5 điểm | #8–9 (Phòng), #25–26 (Khách) ⇒ **4 chức năng** |
| Sắp xếp (≥ 4) | 2 điểm | #10–13 (Phòng), #27–30 (Khách) ⇒ **8 chức năng** |
| Lớn nhất / nhỏ nhất (≥ 4) | 1 điểm | #14–17 (Phòng), #31–34 (Khách) ⇒ **8 chức năng** |
| Thống kê (≥ 5) | 1 điểm | #35–41 ⇒ **7 chức năng** |
| Menu + Lưu trữ | 1 điểm | Menu phân cấp + đọc/ghi file tự động |

---

*Tài liệu này được xây dựng cho đề tài: Quản lý thuế phòng khách sạn – Môn Cấu trúc dữ liệu và giải thuật IT05*
