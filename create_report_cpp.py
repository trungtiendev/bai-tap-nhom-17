#!/usr/bin/env python3
"""
Tạo báo cáo CTDL - Quản lý thuế phòng khách sạn
Môn: Cấu trúc dữ liệu và giải thuật - IT05, Chủ đề 07
Trường Đại Học Mở Hà Nội
CTDL: Danh sách liên kết đơn (C/C++, class, DSLK đơn)
File kết quả: Bao_cao_CTDL_Chu_de_07_CPP.docx
"""

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

FONT_NAME = 'Times New Roman'
FONT_CODE = 'Courier New'
FONT_SIZE = 13
FONT_SIZE_H1 = 14
FONT_SIZE_H2 = 13

OUTPUT = '/home/hgahc/.openclaw/workspace/ctdl/Bao_cao_CTDL_Chu_de_07_CPP.docx'


def set_run_font(run, name=FONT_NAME, size=FONT_SIZE, bold=False, italic=False, color=None):
    run.font.name = name
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = RGBColor(*color)
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.insert(0, rFonts)
    rFonts.set(qn('w:eastAsia'), name)


def add_paragraph(doc, text='', bold=False, size=FONT_SIZE, align=WD_ALIGN_PARAGRAPH.JUSTIFY,
                  space_after=6, space_before=0, italic=False, color=None, font_name=FONT_NAME):
    p = doc.add_paragraph()
    p.alignment = align
    pf = p.paragraph_format
    pf.space_after = Pt(space_after)
    pf.space_before = Pt(space_before)
    if text:
        run = p.add_run(text)
        set_run_font(run, font_name, size, bold, italic, color)
    return p


def add_heading_like(doc, text, level=1):
    size = FONT_SIZE_H1 if level == 1 else FONT_SIZE_H2
    return add_paragraph(doc, text, bold=True, size=size, space_before=12, space_after=6)


def add_empty(doc, size=6):
    return add_paragraph(doc, '', size=size)


def add_code(doc, lines):
    add_empty(doc)
    for line in lines:
        p = add_paragraph(doc, line, size=11, font_name=FONT_CODE, align=WD_ALIGN_PARAGRAPH.LEFT)
        p.paragraph_format.left_indent = Cm(1)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
    add_empty(doc)


def set_table_style(table):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for ri, row in enumerate(table.rows):
        for cell in row.cells:
            for p in cell.paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER if ri == 0 else WD_ALIGN_PARAGRAPH.LEFT
                for run in p.runs:
                    if ri == 0:
                        run.bold = True
            tc = cell._tc
            tcPr = tc.get_or_add_tcPr()
            tcBorders = OxmlElement('w:tcBorders')
            for edge in ['top', 'left', 'bottom', 'right']:
                el = OxmlElement(f'w:{edge}')
                el.set(qn('w:val'), 'single')
                el.set(qn('w:sz'), '4')
                el.set(qn('w:space'), '0')
                el.set(qn('w:color'), '000000')
                tcBorders.append(el)
            tcPr.append(tcBorders)


def make_table(doc, headers, rows):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    set_table_style(table)
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = h
        shading = OxmlElement('w:shd')
        shading.set(qn('w:fill'), 'D9E2F3')
        shading.set(qn('w:val'), 'clear')
        cell._tc.get_or_add_tcPr().append(shading)
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            table.rows[ri + 1].cells[ci].text = str(val)
    return table


def build():
    doc = Document()

    # Page setup: trên 2cm, dưới 2cm, trái 3cm, phải 2cm
    section = doc.sections[0]
    section.top_margin = Cm(2)
    section.bottom_margin = Cm(2)
    section.left_margin = Cm(3)
    section.right_margin = Cm(2)

    # ==================== TRANG BÌA ====================
    add_empty(doc, 18)
    add_paragraph(doc, 'TRƯỜNG ĐẠI HỌC MỞ HÀ NỘI', align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)
    add_paragraph(doc, 'TRUNG TÂM ĐÀO TẠO ELEARNING', align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)
    add_paragraph(doc, '--------------------', align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    add_empty(doc, 6)
    add_paragraph(doc, '[LOGO TRƯỜNG]', align=WD_ALIGN_PARAGRAPH.CENTER, italic=True, color=(136, 136, 136))
    add_empty(doc, 6)
    add_empty(doc, 6)
    add_paragraph(doc, 'HỌ VÀ TÊN SINH VIÊN – Lớp', align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)
    add_paragraph(doc, '(Danh sách thành viên sắp xếp theo tên)', align=WD_ALIGN_PARAGRAPH.CENTER,
                  italic=True, size=12, space_after=18)
    add_empty(doc, 6)
    add_empty(doc, 6)
    add_paragraph(doc, 'BÀI TẬP LỚN: QUẢN LÝ THUẾ PHÒNG KHÁCH SẠN',
                  bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=12, space_after=12)
    add_empty(doc, 6)
    add_paragraph(doc, 'BÁO CÁO BÀI TẬP LỚN', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)
    add_paragraph(doc, 'MÔN: CẤU TRÚC DỮ LIỆU VÀ GIẢI THUẬT', bold=True, size=14,
                  align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)
    add_empty(doc, 6)
    add_paragraph(doc, 'Giảng viên hướng dẫn: …', space_after=0)
    add_empty(doc, 18)
    add_empty(doc, 6)
    add_paragraph(doc, 'Hà Nội – 2025', align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=14)
    doc.add_page_break()

    # ==================== PHẦN 1: XÁC ĐỊNH BÀI TOÁN ====================
    add_heading_like(doc, '1. XÁC ĐỊNH BÀI TOÁN', 1)
    add_heading_like(doc, '1.1. Mô tả bài toán', 2)
    add_paragraph(doc,
        'Xây dựng chương trình quản lý thuế phòng khách sạn bằng ngôn ngữ C/C++, '
        'sử dụng cấu trúc dữ liệu danh sách liên kết đơn (Singly Linked List). Hệ thống cho phép quản lý '
        'thông tin các phòng khách sạn và khách hàng đang thuê phòng, từ đó tính toán và thống kê thuế phòng. '
        'Chương trình hỗ trợ nhập xuất dữ liệu bằng tay hoặc thông qua file để dữ liệu được lưu trữ bền vững.')

    add_paragraph(doc,
        'Bài toán hướng đến việc ứng dụng các kiến thức về cấu trúc dữ liệu (danh sách liên kết đơn) và '
        'các thuật toán cơ bản (thêm, xóa, sửa, tìm kiếm, sắp xếp, thống kê) để giải quyết một bài toán '
        'thực tế trong quản lý khách sạn. Hai đối tượng chính được quản lý là Phòng (Room) và Khách (Guest).')

    add_heading_like(doc, '1.2. Yêu cầu chi tiết', 2)
    make_table(doc,
        ['STT', 'Nhóm chức năng', 'Yêu cầu tối thiểu', 'Điểm'],
        [
            ['1', 'Nhập/In danh sách, Đọc/Ghi file', '1 bộ nhập-in + đọc-ghi file', '2.0'],
            ['2', 'Tìm, sửa, xóa đối tượng', '-', '1.5'],
            ['3', 'Tìm kiếm đối tượng', '2 yêu cầu', '0.5'],
            ['4', 'Sắp xếp đối tượng', '4 yêu cầu', '2.0'],
            ['5', 'Tìm lớn nhất/nhỏ nhất', '4 yêu cầu', '1.0'],
            ['6', 'Thống kê', '5 yêu cầu', '1.0'],
            ['7', 'Lưu trữ chức năng (tổ chức menu)', '-', '1.0'],
            ['', 'Tổng', '', '10.0'],
        ])
    add_empty(doc)

    add_heading_like(doc, '1.3. Đối tượng quản lý', 2)
    add_paragraph(doc, 'Chương trình quản lý 02 đối tượng chính:')
    add_paragraph(doc, '   1. Phòng khách sạn (Room) – các phòng có sẵn trong khách sạn')
    add_paragraph(doc, '   2. Khách thuê phòng (Guest) – khách hàng đang thuê phòng')
    add_empty(doc)

    # ==================== PHẦN 2: XÁC ĐỊNH CTDL ====================
    add_heading_like(doc, '2. XÁC ĐỊNH CẤU TRÚC DỮ LIỆU BIỂU DIỄN BÀI TOÁN', 1)
    add_heading_like(doc, '2.1. Lựa chọn cấu trúc dữ liệu', 2)
    add_paragraph(doc,
        'Chương trình sử dụng cấu trúc dữ liệu Danh sách liên kết đơn (Singly Linked List).')
    add_paragraph(doc,
        'Lý do chọn: Số lượng phòng và khách thay đổi linh hoạt (thêm/xóa thường xuyên), '
        'DSLK đơn không cần cấp phát tĩnh trước. Thao tác duyệt tuần tự phù hợp với các yêu cầu '
        'in danh sách, tìm kiếm, thống kê. Bộ nhớ chỉ dùng đúng bằng số phần tử thực tế. '
        'Cài đặt đơn giản, dễ hiểu, phù hợp mức độ sinh viên.')

    add_heading_like(doc, '2.2. Thông tin quản lý của từng đối tượng', 2)
    add_paragraph(doc, 'Đối tượng 1: Phòng khách sạn (Room) – struct Phong', bold=True)
    make_table(doc, ['STT', 'Trường', 'Kiểu dữ liệu', 'Mô tả'],
        [
            ['1', 'maPhong', 'char[20]', 'Mã phòng (vd: P001, P002)'],
            ['2', 'loaiPhong', 'char[30]', 'Loại phòng (Don, Doi, VIP)'],
            ['3', 'giaThue', 'float', 'Giá thuê 1 đêm (VNĐ)'],
            ['4', 'tinhTrang', 'int', '0 = Trống, 1 = Đang thuê'],
            ['5', 'thueSuat', 'float', 'Thuế suất (%)'],
        ])
    add_empty(doc)

    add_paragraph(doc, 'Đối tượng 2: Khách thuê phòng (Guest) – struct Khach', bold=True)
    make_table(doc, ['STT', 'Trường', 'Kiểu dữ liệu', 'Mô tả'],
        [
            ['1', 'maKhach', 'char[20]', 'Mã khách (vd: K001, K002)'],
            ['2', 'hoTen', 'char[60]', 'Họ tên khách hàng'],
            ['3', 'cmnd', 'char[20]', 'Số CMND/CCCD'],
            ['4', 'maPhongThue', 'char[20]', 'Mã phòng đang thuê (liên kết với Phong)'],
            ['5', 'soDem', 'int', 'Số đêm ở'],
            ['6', 'ngayDen', 'char[15]', 'Ngày nhận phòng (dd/mm/yyyy)'],
        ])
    add_empty(doc)

    add_heading_like(doc, '2.3. Định nghĩa CTDL trong C/C++', 2)
    add_code(doc, [
        'typedef struct {',
        '    char maPhong[MAX_MA];       // Ma phong',
        '    char loaiPhong[MAX_LOAI];   // Loai phong (Don/Doi/VIP)',
        '    float giaThue;              // Gia thue 1 dem',
        '    int tinhTrang;              // 0 = Trong, 1 = Dang thue',
        '    float thueSuat;             // Thue suat (%)',
        '} Phong;',
        '',
        'typedef struct {',
        '    char maKhach[MAX_MA];       // Ma khach',
        '    char hoTen[MAX_TEN];        // Ho ten khach',
        '    char cmnd[MAX_MA];          // CMND/CCCD',
        '    char maPhongThue[MAX_MA];   // Ma phong dang thue',
        '    int soDem;                  // So dem o',
        '    char ngayDen[MAX_NGAY];     // Ngay den (dd/mm/yyyy)',
        '} Khach;',
        '',
        'typedef struct Node {',
        '    Phong phong;                // Du lieu phong',
        '    Khach khach;                // Du lieu khach',
        '    int loai;                   // 0 = Phong, 1 = Khach',
        '    struct Node *next;          // Con tro nut ke tiep',
        '} Node;',
        '',
        'typedef struct {',
        '    Node *dau;                  // Con tro dau danh sach',
        '    int soPhong;                // So luong phong',
        '    int soKhach;                // So luong khach',
        '} LinkedList;',
    ])

    add_heading_like(doc, '2.4. Input và Output của bài toán', 2)
    make_table(doc, ['Thành phần', 'Mô tả'],
        [
            ['Input từ bàn phím', 'Thông tin phòng (mã, loại, giá, tình trạng, thuế suất); '
             'thông tin khách (mã, họ tên, CMND, mã phòng thuê, số đêm, ngày đến)'],
            ['Input từ file', 'rooms.txt: danh sách phòng; guests.txt: danh sách khách'],
            ['Output màn hình', 'Danh sách phòng, khách, kết quả tìm kiếm, sắp xếp, thống kê dạng bảng'],
            ['Output file', 'Ghi dữ liệu phòng ra rooms.txt; ghi khách ra guests.txt'],
            ['Giao diện', 'Menu chính và menu con tương tác với người dùng'],
        ])
    add_empty(doc)
    doc.add_page_break()

    # ==================== PHẦN 3: XÁC ĐỊNH THUẬT TOÁN ====================
    add_heading_like(doc, '3. XÁC ĐỊNH CÁC THUẬT TOÁN', 1)
    add_heading_like(doc, '3.1. Các hàm xử lý danh sách (nền tảng)', 2)
    make_table(doc, ['STT', 'Hàm', 'Mô tả'],
        [
            ['1', 'khoiTao(L)', 'Khởi tạo danh sách rỗng (dau=NULL, soPhong=0, soKhach=0)'],
            ['2', 'themPhongDau(L, p)', 'Thêm phòng vào đầu DSLK'],
            ['3', 'themKhachDau(L, k)', 'Thêm khách vào đầu DSLK'],
            ['4', 'xoaPhong(L, ma)', 'Xóa phòng theo mã'],
            ['5', 'xoaKhach(L, ma)', 'Xóa khách theo mã'],
            ['6', 'timPhongTheoMa(L, ma)', 'Tìm phòng theo mã, trả về Node*'],
            ['7', 'timKhachTheoCMND(L, cmnd)', 'Tìm khách theo CMND, trả về Node*'],
            ['8', 'huyDS(L)', 'Giải phóng toàn bộ danh sách'],
        ])
    add_empty(doc)

    add_heading_like(doc, '3.2. Các chức năng với đối tượng Phòng', 2)
    add_paragraph(doc, 'Nhập – In – Đọc/Ghi file (2 điểm):', bold=True)
    make_table(doc, ['STT', 'Chức năng', 'Mô tả'],
        [
            ['1', 'nhapPhong(&p)', 'Nhập 1 phòng từ bàn phím. Kiểm tra giá>0, thuế>=0, trạng thái 0/1'],
            ['2', 'inDSPhong(L)', 'In danh sách phòng ra màn hình dạng bảng'],
            ['3', 'docFilePhong(L)', 'Đọc danh sách phòng từ file rooms.txt'],
            ['4', 'luuFilePhong(L)', 'Ghi danh sách phòng vào file rooms.txt'],
        ])
    add_empty(doc)

    add_paragraph(doc, 'Tìm – Sửa – Xóa (1.5 điểm):', bold=True)
    make_table(doc, ['STT', 'Chức năng', 'Mô tả'],
        [
            ['5', 'suaPhong(L)', 'Sửa thông tin phòng: nhập mã, tìm, nhập lại thông tin mới'],
            ['6', 'xoaPhong(L)', 'Xóa phòng theo mã: duyệt DSLK, cập nhật liên kết, free'],
        ])
    add_empty(doc)

    add_paragraph(doc, 'Tìm kiếm (0.5 điểm – tối thiểu 2):', bold=True)
    make_table(doc, ['STT', 'Chức năng', 'Mô tả'],
        [
            ['7', 'timPhongTheoMa(L, ma)', 'Tìm phòng theo mã (không phân biệt HOA/thường – strcasecmp)'],
            ['8', 'timPhongTheoLoai(L)', 'Tìm tất cả phòng theo loại (Don/Doi/VIP)'],
        ])
    add_empty(doc)

    add_paragraph(doc, 'Sắp xếp (2 điểm – tối thiểu 4 yêu cầu):', bold=True)
    make_table(doc, ['STT', 'Chức năng', 'Ý nghĩa'],
        [
            ['9', 'sapXepPhongGiaTang(L)', 'Sắp xếp phòng theo giá thuê tăng dần'],
            ['10', 'sapXepPhongGiaGiam(L)', 'Sắp xếp phòng theo giá thuê giảm dần'],
            ['11', 'sapXepPhongMaTang(L)', 'Sắp xếp phòng theo mã phòng tăng dần (A→Z)'],
        ])
    add_empty(doc)

    add_paragraph(doc,
        'Thuật toán sắp xếp: Sử dụng Bubble Sort trên DSLK đơn. Đổi dữ liệu giữa các nút bằng hàm '
        'swapNode(), không thay đổi liên kết next. Thuật toán dùng biến last để giới hạn vùng đã sắp xếp.',
        italic=True)
    add_empty(doc)

    add_paragraph(doc, 'Tìm lớn nhất / nhỏ nhất (1 điểm – tối thiểu 4 yêu cầu):', bold=True)
    make_table(doc, ['STT', 'Chức năng', 'Mô tả'],
        [
            ['12', 'phongGiaCaoNhat(L)', 'Tìm phòng có giá thuê cao nhất (maxG)'],
            ['13', 'phongGiaThapNhat(L)', 'Tìm phòng có giá thuê thấp nhất (minG)'],
        ])
    add_empty(doc)

    add_heading_like(doc, '3.3. Các chức năng với đối tượng Khách', 2)
    add_paragraph(doc, 'Nhập – In – Đọc/Ghi file:', bold=True)
    make_table(doc, ['STT', 'Chức năng', 'Mô tả'],
        [
            ['14', 'nhapKhach(&k)', 'Nhập thông tin khách: mã, họ tên, CMND, mã phòng, số đêm, ngày đến'],
            ['15', 'inDSKhach(L)', 'In danh sách khách ra màn hình dạng bảng'],
            ['16', 'docFileKhach(L)', 'Đọc danh sách khách từ file guests.txt'],
            ['17', 'luuFileKhach(L)', 'Ghi danh sách khách vào file guests.txt'],
        ])
    add_empty(doc)

    add_paragraph(doc, 'Tìm – Sửa – Xóa:', bold=True)
    make_table(doc, ['STT', 'Chức năng', 'Mô tả'],
        [
            ['18', 'suaKhach(L)', 'Sửa thông tin khách theo mã'],
            ['19', 'xoaKhach(L)', 'Xóa khách theo mã'],
        ])
    add_empty(doc)

    add_paragraph(doc, 'Tìm kiếm (tối thiểu 2 yêu cầu):', bold=True)
    make_table(doc, ['STT', 'Chức năng', 'Mô tả'],
        [
            ['20', 'timKhachTheoCMND(L, cmnd)', 'Tìm khách theo số CMND (so sánh chính xác – strcmp)'],
            ['21', 'timKhachTheoTen(L)', 'Tìm khách theo họ tên (tìm gần đúng – strstr)'],
        ])
    add_empty(doc)

    add_paragraph(doc, 'Sắp xếp:', bold=True)
    make_table(doc, ['STT', 'Chức năng', 'Mô tả'],
        [
            ['22', 'sapXepKhachTen(L)', 'Sắp xếp khách theo tên A→Z (strcasecmp)'],
        ])
    add_empty(doc)

    add_paragraph(doc, 'Tìm lớn nhất / nhỏ nhất:', bold=True)
    make_table(doc, ['STT', 'Chức năng', 'Mô tả'],
        [
            ['23', 'khachOLauNhat(L)', 'Tìm khách có số đêm ở nhiều nhất'],
            ['24', 'khachMoiNhat(L)', 'Tìm khách có số đêm ở ít nhất (khách đầu DSLK)'],
        ])
    add_empty(doc)

    add_heading_like(doc, '3.4. Thống kê (1 điểm – tối thiểu 5 yêu cầu)', 2)
    make_table(doc, ['STT', 'Chức năng', 'Mô tả'],
        [
            ['25', 'thongKe(L)', 'Thống kê tổng quan: tổng phòng, phòng đang thuê, phòng trống, '
             'phân loại Don/Doi/VIP, tổng khách, tổng doanh thu thuế'],
        ])
    add_empty(doc)
    add_paragraph(doc,
        'Công thức tính doanh thu thuế: doanhThu = soDem * giaThue * thueSuat / 100.0. '
        'Hàm thongKe duyệt toàn bộ DSLK một lần, với mỗi Node có loai==1 (khách) sẽ tìm phòng '
        'tương ứng theo maPhongThue để lấy giaThue và thueSuat.')
    add_empty(doc)

    add_heading_like(doc, '3.5. Tổ chức menu chương trình (1 điểm)', 2)
    add_paragraph(doc, 'Menu chính:', bold=True)
    add_code(doc, [
        '+---------------------- QUAN LY THUE PHONG KHACH SAN ----------------------+',
        '| 1. Quan ly Phong      2. Quan ly Khach      3. Sap xep                |',
        '| 4. Tim Max/Min        5. Thong ke           6. Luu file               |',
        '| 7. Doc file           0. Thoat                                         |',
        '+------------------------------------------------------------------------------+',
    ])

    add_paragraph(doc, 'Menu con Quản lý Phòng:', bold=True)
    add_code(doc, [
        '--- QUAN LY PHONG ---',
        '1.Them 2.Hien thi 3.Tim theo ma 4.Tim theo loai',
        '5.Sua 6.Xoa 0.Quay lai',
    ])

    add_paragraph(doc, 'Menu con Quản lý Khách:', bold=True)
    add_code(doc, [
        '--- QUAN LY KHACH ---',
        '1.Them 2.Hien thi 3.Tim theo CMND 4.Tim theo ten',
        '5.Sua 6.Xoa 0.Quay lai',
    ])

    add_paragraph(doc, 'Menu con Sắp xếp:', bold=True)
    add_code(doc, [
        '--- SAP XEP ---',
        '1.Phong gia tang 2.Phong gia giam 3.Phong theo ma',
        '4.Khach theo ten 0.Quay lai',
    ])

    add_paragraph(doc, 'Menu con Tìm Max/Min:', bold=True)
    add_code(doc, [
        '--- TIM MAX/MIN ---',
        '1.Phong gia cao nhat 2.Phong gia thap nhat',
        '3.Khach o lau nhat 4.Khach moi nhat 0.Quay lai',
    ])

    add_heading_like(doc, '3.6. Xử lý lỗi nhập liệu', 2)
    make_table(doc, ['STT', 'Tình huống', 'Xử lý'],
        [
            ['1', 'Giá thuê ≤ 0', 'Yêu cầu nhập lại, giá thuê phải > 0'],
            ['2', 'Thuế suất < 0', 'Yêu cầu nhập lại, thuế suất >= 0'],
            ['3', 'Tình trạng không phải 0 hoặc 1', 'Yêu cầu nhập lại (0=Trống, 1=Đang thuê)'],
            ['4', 'Số đêm ≤ 0', 'Yêu cầu nhập lại, số đêm phải > 0'],
            ['5', 'Nhập sai kiểu dữ liệu (chữ vào số)', 'Dùng fgets + vòng lặp kiểm tra laSo/laSoThuc'],
            ['6', 'File không tồn tại khi đọc', 'Thông báo lỗi, tạo danh sách rỗng'],
        ])
    add_empty(doc)

    add_heading_like(doc, '3.7. Định dạng file lưu trữ', 2)
    add_paragraph(doc, 'File rooms.txt (các trường phân cách bằng dấu |):', bold=True)
    add_code(doc, [
        '<maPhong>|<loaiPhong>|<giaThue>|<tinhTrang>|<thueSuat>',
        'P001|Don|500000.00|1|5.00',
        'P002|Doi|800000.00|1|8.00',
        'P003|VIP|2000000.00|0|10.00',
    ])

    add_paragraph(doc, 'File guests.txt:', bold=True)
    add_code(doc, [
        '<maKhach>|<hoTen>|<cmnd>|<maPhongThue>|<soDem>|<ngayDen>',
        'K001|Nguyen Van A|123456789|P001|3|01/03/2025',
        'K002|Tran Thi B|987654321|P002|5|28/02/2025',
    ])
    add_empty(doc)
    doc.add_page_break()

    # ==================== PHẦN 4: LẬP TRÌNH – CÀI ĐẶT ====================
    add_heading_like(doc, '4. LẬP TRÌNH – CÀI ĐẶT', 1)
    add_heading_like(doc, '4.1. Cấu trúc chương trình', 2)
    add_paragraph(doc, 'Chương trình được tổ chức thành các module chính sau:')
    make_table(doc, ['Module', 'Mô tả'],
        [
            ['Khai báo thư viện và hằng số', '#include <stdio.h>, <stdlib.h>, <string.h>, <ctype.h>; '
             '#define MAX_MA 20, MAX_TEN 60, MAX_LOAI 30, MAX_NGAY 15'],
            ['Định nghĩa cấu trúc dữ liệu', 'Struct Phong, Khach, Node, LinkedList'],
            ['Hàm nhập liệu', 'nhapPhong(), nhapKhach() – có kiểm tra lỗi nhập'],
            ['Hàm xử lý DSLK', 'themPhongDau(), themKhachDau(), xoaPhong(), xoaKhach(), timKiem()'],
            ['Hàm hiển thị', 'hienThiPhong(), hienThiKhach(), inDSPhong(), inDSKhach()'],
            ['Hàm file', 'docFilePhong(), docFileKhach(), luuFilePhong(), luuFileKhach()'],
            ['Hàm sắp xếp', 'sapXepPhongGiaTang(), sapXepPhongGiaGiam(), sapXepPhongMaTang(), sapXepKhachTen()'],
            ['Hàm Max/Min', 'phongGiaCaoNhat(), phongGiaThapNhat(), khachOLauNhat(), khachMoiNhat()'],
            ['Hàm thống kê', 'thongKe() – thống kê tổng quan'],
            ['Menu', 'hienThiMenu(), menuPhong(), menuKhach(), menuSapXep(), menuMaxMin()'],
            ['Hàm main', 'Khởi tạo, đọc file tự động, vòng lặp menu chính'],
        ])
    add_empty(doc)

    add_heading_like(doc, '4.2. Các hàm xử lý DSLK cơ bản', 2)
    add_paragraph(doc, 'Khởi tạo và tạo Node:', bold=True)
    add_code(doc, [
        'void khoiTao(LinkedList *l) {',
        '    l->dau = NULL;',
        '    l->soPhong = 0;',
        '    l->soKhach = 0;',
        '}',
        '',
        'Node* taoNodePhong(Phong p) {',
        '    Node *n = (Node*)malloc(sizeof(Node));',
        '    if(!n) { printf("Loi cap phat!\\n"); return NULL; }',
        '    n->phong = p;',
        '    n->loai = 0;      // 0 = Phong',
        '    n->next = NULL;',
        '    return n;',
        '}',
        '',
        'Node* taoNodeKhach(Khach k) {',
        '    Node *n = (Node*)malloc(sizeof(Node));',
        '    if(!n) { printf("Loi cap phat!\\n"); return NULL; }',
        '    n->khach = k;',
        '    n->loai = 1;      // 1 = Khach',
        '    n->next = NULL;',
        '    return n;',
        '}',
    ])

    add_paragraph(doc, 'Thêm nút vào đầu danh sách:', bold=True)
    add_code(doc, [
        'void themPhongDau(LinkedList *l, Phong p) {',
        '    Node *n = taoNodePhong(p);',
        '    if(!n) return;',
        '    n->next = l->dau;',
        '    l->dau = n;',
        '    l->soPhong++;',
        '}',
        '',
        'void themKhachDau(LinkedList *l, Khach k) {',
        '    Node *n = taoNodeKhach(k);',
        '    if(!n) return;',
        '    n->next = l->dau;',
        '    l->dau = n;',
        '    l->soKhach++;',
        '}',
    ])

    add_paragraph(doc, 'Xóa nút khỏi DSLK:', bold=True)
    add_code(doc, [
        'void xoaPhong(LinkedList *l) {',
        '    char ma[30];',
        '    printf("Nhap ma phong can xoa: ");',
        '    fgets(ma, 30, stdin); xoaXuongDong(ma); chuanHoa(ma);',
        '    Node *p = NULL, *cur = l->dau;',
        '    while(cur) {',
        '        if(cur->loai == 0 &&',
        '           strcasecmp(cur->phong.maPhong, ma) == 0) {',
        '            if(!p) l->dau = cur->next;',
        '            else p->next = cur->next;',
        '            free(cur); l->soPhong--;',
        '            printf("Da xoa!\\n"); return;',
        '        }',
        '        p = cur; cur = cur->next;',
        '    }',
        '    printf("Khong tim thay!\\n");',
        '}',
    ])

    add_paragraph(doc, 'Hàm swapNode (đổi dữ liệu 2 nút, dùng cho Bubble Sort):', bold=True)
    add_code(doc, [
        'void swapNode(Node *a, Node *b) {',
        '    Phong tp = a->phong;',
        '    Khach tk = a->khach;',
        '    int tl = a->loai;',
        '    a->phong = b->phong;',
        '    a->khach = b->khach;',
        '    a->loai = b->loai;',
        '    b->phong = tp;',
        '    b->khach = tk;',
        '    b->loai = tl;',
        '}',
    ])

    add_paragraph(doc, 'Sắp xếp Bubble Sort trên DSLK:', bold=True)
    add_code(doc, [
        'void sapXepPhongGiaTang(LinkedList *l) {',
        '    if(!l->dau || !l->dau->next) return;',
        '    int sw; Node *p, *last = NULL;',
        '    do {',
        '        sw = 0; p = l->dau;',
        '        while(p->next != last) {',
        '            if(p->loai == 0 && p->next->loai == 0',
        '               && p->phong.giaThue > p->next->phong.giaThue) {',
        '                swapNode(p, p->next); sw = 1;',
        '            }',
        '            p = p->next;',
        '        }',
        '        last = p;',
        '    } while(sw);',
        '    printf("Da sap xep phong gia tang.\\n");',
        '    inDSPhong(l);',
        '}',
    ])

    add_paragraph(doc, 'Nhập dữ liệu có kiểm tra lỗi:', bold=True)
    add_code(doc, [
        'void nhapPhong(Phong *p) {',
        '    char tam[200];',
        '    printf("  Ma phong: ");',
        '    fgets(tam, 200, stdin);',
        '    xoaXuongDong(tam); chuanHoa(tam);',
        '    strcpy(p->maPhong, tam);',
        '    printf("  Loai phong (Don/Doi/VIP): ");',
        '    fgets(tam, 200, stdin);',
        '    xoaXuongDong(tam); chuanHoa(tam);',
        '    strcpy(p->loaiPhong, tam);',
        '    do {',
        '        printf("  Gia thue 1 dem: ");',
        '        fgets(tam, 200, stdin);',
        '        xoaXuongDong(tam); chuanHoa(tam);',
        '        if(!laSoThuc(tam) || atof(tam) <= 0)',
        '            { printf("  >> Loi: Gia thue >0!\\n"); continue; }',
        '        p->giaThue = atof(tam); break;',
        '    } while(1);',
        '    // ... tuong tu cho thueSuat, tinhTrang',
        '}',
    ])

    add_paragraph(doc, 'Đọc/Ghi file:', bold=True)
    add_code(doc, [
        'void docFilePhong(LinkedList *l) {',
        '    FILE *f = fopen("rooms.txt", "r");',
        '    if(!f) { printf("Khong co file rooms.txt.\\n"); return; }',
        '    Phong p; int d = 0;',
        '    while(fscanf(f, "%[^|]|%[^|]|%f|%d|%f\\n",',
        '          p.maPhong, p.loaiPhong, &p.giaThue,',
        '          &p.tinhTrang, &p.thueSuat) == 5) {',
        '        themPhongDau(l, p); d++;',
        '    }',
        '    fclose(f); printf("Da doc %d phong\\n", d);',
        '}',
        '',
        'void luuFilePhong(LinkedList *l) {',
        '    FILE *f = fopen("rooms.txt", "w");',
        '    if(!f) { printf("Loi mo file!\\n"); return; }',
        '    Node *cur = l->dau;',
        '    while(cur) {',
        '        if(cur->loai == 0)',
        '            fprintf(f, "%s|%s|%.2f|%d|%.2f\\n",',
        '                cur->phong.maPhong, cur->phong.loaiPhong,',
        '                cur->phong.giaThue, cur->phong.tinhTrang,',
        '                cur->phong.thueSuat);',
        '        cur = cur->next;',
        '    }',
        '    fclose(f);',
        '    printf("Da luu %d phong vao rooms.txt\\n", l->soPhong);',
        '}',
    ])

    add_paragraph(doc, 'Thống kê:', bold=True)
    add_code(doc, [
        'void thongKe(LinkedList *l) {',
        '    int tt = l->soPhong, tk = l->soKhach;',
        '    int dThue = 0, tTrong = 0;',
        '    int dDon = 0, dDoi = 0, dVIP = 0;',
        '    float doanhThu = 0;',
        '    Node *cur = l->dau;',
        '    while(cur) {',
        '        if(cur->loai == 0) {',
        '            if(cur->phong.tinhTrang == 1) dThue++;',
        '            else tTrong++;',
        '            if(strcasecmp(cur->phong.loaiPhong, "don")==0) dDon++;',
        '            else if(strcasecmp(cur->phong.loaiPhong, "doi")==0) dDoi++;',
        '            else if(strcasecmp(cur->phong.loaiPhong, "vip")==0) dVIP++;',
        '        }',
        '        if(cur->loai == 1) {',
        '            Node *p = l->dau;',
        '            float g = 0, th = 0;',
        '            while(p) {',
        '                if(p->loai == 0 &&',
        '                   strcasecmp(p->phong.maPhong,',
        '                       cur->khach.maPhongThue) == 0) {',
        '                    g = p->phong.giaThue;',
        '                    th = p->phong.thueSuat;',
        '                    break;',
        '                }',
        '                p = p->next;',
        '            }',
        '            doanhThu += cur->khach.soDem * g * th / 100.0;',
        '        }',
        '        cur = cur->next;',
        '    }',
        '    printf("\\n========== THONG KE ==========\\n");',
        '    printf("  Tong so phong:       %d\\n", tt);',
        '    printf("  Phong dang thue:     %d\\n", dThue);',
        '    printf("  Phong trong:         %d\\n", tTrong);',
        '    printf("  Phong loai Don:      %d\\n", dDon);',
        '    printf("  Phong loai Doi:      %d\\n", dDoi);',
        '    printf("  Phong loai VIP:      %d\\n", dVIP);',
        '    printf("  Tong so khach:       %d\\n", tk);',
        '    printf("  Tong doanh thu thue: %.0f VND\\n", doanhThu);',
        '    printf("==============================\\n");',
        '}',
    ])

    add_heading_like(doc, '4.3. Hàm main và tổ chức menu', 2)
    add_code(doc, [
        'int main() {',
        '    LinkedList list;',
        '    khoiTao(&list);',
        '    docFilePhong(&list);',
        '    docFileKhach(&list);',
        '    int chon; char tam[10];',
        '    do {',
        '        hienThiMenu();',
        '        fgets(tam, 10, stdin);',
        '        chon = atoi(tam);',
        '        switch(chon) {',
        '            case 1: menuPhong(&list); break;',
        '            case 2: menuKhach(&list); break;',
        '            case 3: menuSapXep(&list); break;',
        '            case 4: menuMaxMin(&list); break;',
        '            case 5: thongKe(&list); break;',
        '            case 6: luuFilePhong(&list);',
        '                   luuFileKhach(&list); break;',
        '            case 7: docFilePhong(&list);',
        '                   docFileKhach(&list); break;',
        '            case 0: luuFilePhong(&list);',
        '                   luuFileKhach(&list);',
        '                   huyDS(&list);',
        '                   printf("Cam on!\\n"); break;',
        '            default: printf("Chon sai!\\n");',
        '        }',
        '    } while(chon != 0);',
        '    return 0;',
        '}',
    ])

    add_empty(doc)
    doc.add_page_break()

    # ==================== PHẦN 5: KIỂM THỬ ====================    # ==================== PHẦN 5: KIỂM THỬ ====================
    add_heading_like(doc, '5. KIỂM THỬ - LẬP BỘ TEST', 1)
    add_heading_like(doc, '5.1. Bộ dữ liệu mẫu', 2)

    add_paragraph(doc, 'Dữ liệu phòng mẫu:', bold=True)
    make_table(doc,
        ['Mã phòng', 'Loại', 'Giá thuê', 'Trạng thái', 'Thuế suất'],
        [
            ['P001', 'Đơn', '500,000 VND', 'Có khách', '5%'],
            ['P002', 'Đôi', '800,000 VND', 'Có khách', '8%'],
            ['P003', 'VIP', '2,000,000 VND', 'Trống', '10%'],
            ['P004', 'Đôi', '750,000 VND', 'Trống', '5%'],
            ['P005', 'Đơn', '450,000 VND', 'Có khách', '5%'],
        ])
    add_empty(doc)

    add_paragraph(doc, 'Dữ liệu khách mẫu:', bold=True)
    make_table(doc,
        ['Mã khách', 'Họ tên', 'CMND', 'Mã phòng', 'Số đêm', 'Ngày đến'],
        [
            ['K001', 'Nguyễn Văn A', '123456789', 'P001', '3', '01/03/2025'],
            ['K002', 'Trần Thị B', '987654321', 'P002', '5', '28/02/2025'],
            ['K003', 'Lê Văn C', '456789123', 'P005', '2', '05/03/2025'],
        ])
    add_empty(doc)

    add_heading_like(doc, '5.2. Kết quả kiểm thử', 2)
    add_paragraph(doc, '[Chụp ảnh màn hình kết quả chương trình cho từng chức năng tại đây]',
                  italic=True, color=(136,136,136))
    add_empty(doc)

    add_paragraph(doc, '1. Thêm phòng P006:', bold=True)
    add_code(doc, [
        '--- QUAN LY PHONG ---',
        '1.Them 2.Hien thi 3.Tim theo ma ...',
        'Chon: 1',
        '  Ma phong: P006',
        '  Loai phong (Don/Doi/VIP): VIP',
        '  Gia thue 1 dem: 3000000',
        '  Thue suat (%): 12',
        '  Tinh trang (0:Trong, 1:Dang thue): 0',
    ])

    add_paragraph(doc, '2. Hiển thị danh sách phòng:', bold=True)
    add_code(doc, [
        '==================== DANH SACH PHONG ====================',
        'Ma phong     | Loai            |    Gia thue | Trang thai | Thue suat',
        '---------------------------------------------------------------------',
        'P006         | VIP             |     3000000 |      Trong |   12.00%',
        'P005         | Don             |      450000 |  Co khach  |    5.00%',
        'P004         | Doi             |      750000 |      Trong |    5.00%',
        'P003         | VIP             |     2000000 |      Trong |   10.00%',
        'P002         | Doi             |      800000 |  Co khach  |    8.00%',
        'P001         | Don             |      500000 |  Co khach  |    5.00%',
        '---------------------------------------------------------------------',
        'Tong: 6 phong',
    ])

    add_paragraph(doc, '3. Phòng giá cao nhất:', bold=True)
    add_code(doc, [
        '=== PHONG GIA CAO NHAT (3000000 VND) ===',
        'P006 - VIP - Trong',
    ])

    add_paragraph(doc, '4. Thống kê tổng quan:', bold=True)
    add_code(doc, [
        '========== THONG KE ==========',
        '  Tong so phong:       6',
        '  Phong dang thue:     3',
        '  Phong trong:         3',
        '  Tong so khach:       3',
        '  Tong doanh thu thue: 155000 VND',
        '==============================',
    ])

    # ==================== PHẦN 6 ====================
    add_heading_like(doc, '6. TỐI ƯU HÓA CHƯƠNG TRÌNH', 1)
    add_paragraph(doc, 'Hiện tại chương trình chưa có tối ưu đáng kể. Có thể cải thiện trong tương lai:', italic=True)
    add_paragraph(doc, '1. Sử dụng smart pointer (unique_ptr, shared_ptr) thay vì new/delete.')
    add_paragraph(doc, '2. Thay Bubble Sort bằng std::sort với custom comparator.')
    add_paragraph(doc, '3. Dùng std::map để tra cứu nhanh phòng theo mã.')
    add_paragraph(doc, '4. Lưu file nhị phân thay vì text để tăng tốc đọc/ghi.')
    add_empty(doc)

    # ==================== TÀI LIỆU THAM KHẢO ====================
    add_heading_like(doc, 'TÀI LIỆU THAM KHẢO', 1)
    add_paragraph(doc, '[1] Giáo trình Cấu trúc dữ liệu và Giải thuật - Đại học Mở Hà Nội')
    add_paragraph(doc, '[2] Bjarne Stroustrup, The C++ Programming Language, 4th Edition')
    add_paragraph(doc, '[3] https://en.cppreference.com/w/cpp/container/list')
    add_paragraph(doc, '[4] https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_li%C3%AAn_k%E1%BA%BFt')

    # ==================== SAVE ====================
    doc.save(OUTPUT)
    import os
    print(f'OK: {OUTPUT} ({os.path.getsize(OUTPUT)} bytes)')

if __name__ == '__main__':
    build()
