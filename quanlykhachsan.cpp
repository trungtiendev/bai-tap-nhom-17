/*
 * CHUONG TRINH QUAN LY THUE PHONG KHACH SAN - C++
 * Mon: Cau truc du lieu va giai thuat - IT05, Chu de 07
 * Truong Dai Hoc Mo Ha Noi
 * CTDL: Danh sach lien ket don
 * 2 doi tuong: Phong, Khach
 * Ngon ngu: C++17
 *
 * Bo sung cau 3 (kiem tra van dap):
 *  - In thong tin phan tu thu k tu dau danh sach
 *  - Ap dung cho ca danh sach phong va danh sach khach
 */
#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <limits>

using namespace std;

// ==================== KHAI BAO LOP ====================

class Room {
public:
 string maPhong;
 string loaiPhong;
 double giaThue;
 int tinhTrang; // 0: Trong, 1: Dang thue
 double thueSuat;

 Room() : maPhong(""), loaiPhong(""), giaThue(0), tinhTrang(0), thueSuat(0) {}
 Room(string mp, string lp, double gt, int tt, double ts)
 : maPhong(mp), loaiPhong(lp), giaThue(gt), tinhTrang(tt), thueSuat(ts) {}
};

class Guest {
public:
 string maKhach;
 string hoTen;
 string cmnd;
 string maPhongThue;
 int soDem;
 string ngayDen;

 Guest() : maKhach(""), hoTen(""), cmnd(""), maPhongThue(""), soDem(0), ngayDen("") {}
 Guest(string mk, string ht, string cm, string mpt, int sd, string nd)
 : maKhach(mk), hoTen(ht), cmnd(cm), maPhongThue(mpt), soDem(sd), ngayDen(nd) {}
};

// Node cho DSLK don
template <typename T>
class Node {
public:
 T data;
 Node<T>* next;
 Node(T d) : data(d), next(nullptr) {}
};

// Lop danh sach lien ket don
template <typename T>
class LinkedList {
private:
 Node<T>* head;
 int count;

public:
 LinkedList() : head(nullptr), count(0) {}
 ~LinkedList() { clear(); }

 void clear() {
 while (head != nullptr) {
 Node<T>* temp = head;
 head = head->next;
 delete temp;
 }
 count = 0;
 }

 void addHead(T data) {
 Node<T>* node = new Node<T>(data);
 node->next = head;
 head = node;
 count++;
 }

 void addTail(T data) {
 Node<T>* node = new Node<T>(data);
 if (head == nullptr) {
 head = node;
 } else {
 Node<T>* cur = head;
 while (cur->next != nullptr) cur = cur->next;
 cur->next = node;
 }
 count++;
 }

 bool isEmpty() const { return head == nullptr; }
 int size() const { return count; }
 Node<T>* getHead() const { return head; }

 // Xoa theo dieu kien (ham lambda)
 bool removeIf(bool (*condition)(T)) {
 Node<T>* prev = nullptr;
 Node<T>* cur = head;
 while (cur != nullptr) {
 if (condition(cur->data)) {
 if (prev == nullptr) head = cur->next;
 else prev->next = cur->next;
 delete cur;
 count--;
 return true;
 }
 prev = cur;
 cur = cur->next;
 }
 return false;
 }

 // Sap xep bubble sort (hoan doi data)
 void sort(bool (*compare)(T, T)) {
 if (head == nullptr || head->next == nullptr) return;
 bool swapped;
 Node<T>* ptr;
 Node<T>* last = nullptr;
 do {
 swapped = false;
 ptr = head;
 while (ptr->next != last) {
 if (compare(ptr->data, ptr->next->data)) {
 T temp = ptr->data;
 ptr->data = ptr->next->data;
 ptr->next->data = temp;
 swapped = true;
 }
 ptr = ptr->next;
 }
 last = ptr;
 } while (swapped);
 }

 // Tim max/min
 Node<T>* findMax(bool (*better)(T, T)) const {
 if (head == nullptr) return nullptr;
 Node<T>* best = head;
 Node<T>* cur = head->next;
 while (cur != nullptr) {
 if (better(cur->data, best->data)) best = cur;
 cur = cur->next;
 }
 return best;
 }

 Node<T>* findMin(bool (*worse)(T, T)) const {
 return findMax(worse);
 }

 // Tim kiem
 Node<T>* find(bool (*match)(T)) const {
 Node<T>* cur = head;
 while (cur != nullptr) {
 if (match(cur->data)) return cur;
 cur = cur->next;
 }
 return nullptr;
 }
};

// ==================== DICH VU XU LY ====================

void xoaKhoangTrang(string &s) {
 // Xoa dau
 size_t start = s.find_first_not_of(" \t\r\n");
 if (start == string::npos) { s = ""; return; }
 size_t end = s.find_last_not_of(" \t\r\n");
 s = s.substr(start, end - start + 1);
}

bool laSo(const string &s) {
 if (s.empty()) return false;
 for (char c : s) if (!isdigit(c)) return false;
 return true;
}

bool laSoThuc(const string &s) {
 if (s.empty()) return false;
 int cham = 0;
 for (char c : s) {
 if (c == '.') { cham++; if (cham > 1) return false; }
 else if (!isdigit(c)) return false;
 }
 return true;
}

string chuanHoaTen(string s) {
 stringstream ss(s);
 string word, result;
 while (ss >> word) {
 word[0] = toupper(word[0]);
 for (size_t i = 1; i < word.length(); i++)
 word[i] = tolower(word[i]);
 result += word + " ";
 }
 if (!result.empty()) result.pop_back();
 return result;
}

// ==================== DICH VU NHAP LIEU ====================

string nhapString(const string &msg) {
 string s;
 cout << msg;
 getline(cin, s);
 xoaKhoangTrang(s);
 return s;
}

int nhapInt(const string &msg, int minV, int maxV) {
 string s;
 while (true) {
 cout << msg;
 getline(cin, s);
 xoaKhoangTrang(s);
 if (!laSo(s)) {
 cout << " >> Loi: Vui long nhap so nguyen!\n";
 continue;
 }
 int val = stoi(s);
 if (val < minV || val > maxV) {
 cout << " >> Loi: Gia tri tu " << minV << " den " << maxV << "!\n";
 continue;
 }
 return val;
 }
}

double nhapDouble(const string &msg, double minV) {
 string s;
 while (true) {
 cout << msg;
 getline(cin, s);
 xoaKhoangTrang(s);
 if (!laSoThuc(s)) {
 cout << " >> Loi: Vui long nhap so thuc!\n";
 continue;
 }
 double val = stod(s);
 if (val < minV) {
 cout << " >> Loi: Gia tri phai >= " << minV << "!\n";
 continue;
 }
 return val;
 }
}

// ==================== LOP QUAN LY ====================

class HotelManager {
private:
 LinkedList<Room> rooms;
 LinkedList<Guest> guests;

 // Dieu kien xoa
 static bool matchRoomByID(Room r) { return false; } // placeholder
 static bool matchGuestByID(Guest g) { return false; }

 static bool compareGiaTang(Room a, Room b) { return a.giaThue > b.giaThue; }
 static bool compareGiaGiam(Room a, Room b) { return a.giaThue < b.giaThue; }
 static bool compareMaPhong(Room a, Room b) { return a.maPhong > b.maPhong; }
 static bool compareTenKhach(Guest a, Guest b) { return a.hoTen > b.hoTen; }

public:
 HotelManager() {
 docFileTuDong();
 }

 ~HotelManager() {
 ghiFileTuDong();
 }

 // ==================== DOC/GHI FILE ====================
 void docFileTuDong() {
 ifstream f("rooms.txt");
 if (f.is_open()) {
 string line;
 while (getline(f, line)) {
 stringstream ss(line);
 string mp, lp, tsStr, gtStr, ttStr;
 getline(ss, mp, '|');
 getline(ss, lp, '|');
 getline(ss, gtStr, '|');
 getline(ss, ttStr, '|');
 getline(ss, tsStr, '|');
 if (!mp.empty()) {
 Room r(mp, lp, stod(gtStr), stoi(ttStr), stod(tsStr));
 rooms.addTail(r);
 }
 }
 f.close();
 if (rooms.size() > 0)
 cout << "Da doc " << rooms.size() << " phong tu file.\n";
 }
 ifstream fg("guests.txt");
 if (fg.is_open()) {
 string line;
 while (getline(fg, line)) {
 stringstream ss(line);
 string mk, ht, cm, mpt, sdStr, nd;
 getline(ss, mk, '|');
 getline(ss, ht, '|');
 getline(ss, cm, '|');
 getline(ss, mpt, '|');
 getline(ss, sdStr, '|');
 getline(ss, nd, '|');
 if (!mk.empty()) {
 Guest g(mk, ht, cm, mpt, stoi(sdStr), nd);
 guests.addTail(g);
 }
 }
 fg.close();
 if (guests.size() > 0)
 cout << "Da doc " << guests.size() << " khach tu file.\n";
 }
 }

 void ghiFileTuDong() {
 ofstream f("rooms.txt");
 if (f.is_open()) {
 Node<Room>* cur = rooms.getHead();
 while (cur != nullptr) {
 f << cur->data.maPhong << "|"
 << cur->data.loaiPhong << "|"
 << cur->data.giaThue << "|"
 << cur->data.tinhTrang << "|"
 << cur->data.thueSuat << "\n";
 cur = cur->next;
 }
 f.close();
 }
 ofstream fg("guests.txt");
 if (fg.is_open()) {
 Node<Guest>* cur = guests.getHead();
 while (cur != nullptr) {
 fg << cur->data.maKhach << "|"
 << cur->data.hoTen << "|"
 << cur->data.cmnd << "|"
 << cur->data.maPhongThue << "|"
 << cur->data.soDem << "|"
 << cur->data.ngayDen << "\n";
 cur = cur->next;
 }
 fg.close();
 }
 }

 void luuFile() {
 ghiFileTuDong();
 cout << "Da luu du lieu ra file!\n";
 }

 void docFile() {
 rooms.clear();
 guests.clear();
 docFileTuDong();
 }

 // ==================== PHONG ====================
 void themPhong() {
 cout << "\n--- THEM PHONG MOI ---\n";
 string mp = nhapString(" Ma phong: ");
 // Kiem tra trung
 Node<Room>* cur = rooms.getHead();
 while (cur != nullptr) {
 if (cur->data.maPhong == mp) {
 cout << " >> Loi: Ma phong da ton tai!\n";
 return;
 }
 cur = cur->next;
 }
 string lp = nhapString(" Loai phong (Don/Doi/VIP): ");
 double gt = nhapDouble(" Gia thue 1 dem: ", 1);
 double ts = nhapDouble(" Thue suat (%): ", 0);
 int tt = nhapInt(" Tinh trang (0:Trong, 1:Dang thue): ", 0, 1);

 Room r(mp, lp, gt, tt, ts);
 rooms.addTail(r);
 cout << " >> Da them phong " << mp << " thanh cong!\n";
 }

 void inDSPhong() {
 if (rooms.isEmpty()) {
 cout << "\n>> Danh sach phong rong!\n";
 return;
 }
 cout << "\n==================== DANH SACH PHONG ====================\n";
 cout << left << setw(12) << "Ma phong" << " | "
 << setw(16) << "Loai" << " | "
 << right << setw(12) << "Gia thue" << " | "
 << setw(10) << "Trang thai" << " | "
 << setw(8) << "Thue suat" << "\n";
 cout << string(70, '-') << "\n";

 Node<Room>* cur = rooms.getHead();
 while (cur != nullptr) {
 cout << left << setw(12) << cur->data.maPhong << " | "
 << setw(16) << cur->data.loaiPhong << " | "
 << right << setw(12) << fixed << setprecision(0) << cur->data.giaThue << " | "
 << setw(10) << (cur->data.tinhTrang == 0 ? "Trong" : "Co khach") << " | "
 << setw(7) << fixed << setprecision(2) << cur->data.thueSuat << "%\n";
 cur = cur->next;
 }
 cout << string(70, '-') << "\n";
 cout << "Tong: " << rooms.size() << " phong\n";
 }

 void timPhongTheoMa() {
 string mp = nhapString(" Nhap ma phong: ");
 Node<Room>* cur = rooms.getHead();
 while (cur != nullptr) {
 if (cur->data.maPhong == mp) {
 cout << " Tim thay: " << cur->data.maPhong
 << " - " << cur->data.loaiPhong
 << " - " << cur->data.giaThue << " VND"
 << " - " << (cur->data.tinhTrang == 0 ? "Trong" : "Co khach")
 << " - Thue: " << cur->data.thueSuat << "%\n";
 return;
 }
 cur = cur->next;
 }
 cout << " >> Khong tim thay phong!\n";
 }

 void timPhongTheoLoai() {
 string lp = nhapString(" Nhap loai phong: ");
 bool found = false;
 Node<Room>* cur = rooms.getHead();
 cout << "\n=== PHONG LOAI '" << lp << "' ===\n";
 while (cur != nullptr) {
 if (cur->data.loaiPhong == lp) {
 cout << " " << cur->data.maPhong << " - "
 << cur->data.giaThue << " VND - "
 << (cur->data.tinhTrang == 0 ? "Trong" : "Co khach") << "\n";
 found = true;
 }
 cur = cur->next;
 }
 if (!found) cout << " >> Khong tim thay!\n";
 }

 void suaPhong() {
 string mp = nhapString(" Nhap ma phong can sua: ");
 Node<Room>* cur = rooms.getHead();
 while (cur != nullptr) {
 if (cur->data.maPhong == mp) {
 cout << " Dang sua phong " << mp << ":\n";
 cur->data.loaiPhong = nhapString(" Loai phong moi: ");
 cur->data.giaThue = nhapDouble(" Gia thue moi: ", 1);
 cur->data.thueSuat = nhapDouble(" Thue suat moi (%): ", 0);
 cur->data.tinhTrang = nhapInt(" Tinh trang (0:Trong, 1:Dang thue): ", 0, 1);
 cout << " >> Da sua phong " << mp << "!\n";
 return;
 }
 cur = cur->next;
 }
 cout << " >> Khong tim thay!\n";
 }

 void xoaPhong() {
 string mp = nhapString(" Nhap ma phong can xoa: ");
 // Kiem tra co khach dang thue khong
 Node<Guest>* g = guests.getHead();
 while (g != nullptr) {
 if (g->data.maPhongThue == mp) {
 cout << " >> Loi: Phong " << mp << " dang co khach thue, khong the xoa!\n";
 return;
 }
 g = g->next;
 }

 Node<Room>* prev = nullptr;
 Node<Room>* cur = rooms.getHead();
 while (cur != nullptr) {
 if (cur->data.maPhong == mp) {
 if (prev == nullptr) {
 // Cant modify head directly, use addHead/replace trick
 // Simple: remove by rebuilding
 // For simplicity, mark by swapping data
 cout << " >> Chua ho tro xoa phong dau. Dang xu ly...\n";
 return;
 }
 prev->next = cur->next;
 delete cur;
 cout << " >> Da xoa phong " << mp << "!\n";
 return;
 }
 prev = cur;
 cur = cur->next;
 }
 }
 // Overload - xoa bang cach xay dung lai (don gian hon)
 void xoaPhong2() {
 string mp = nhapString(" Nhap ma phong can xoa: ");
 // Kiem tra khach
 Node<Guest>* g = guests.getHead();
 while (g != nullptr) {
 if (g->data.maPhongThue == mp) {
 cout << " >> Loi: Phong " << mp << " dang co khach thue!\n";
 return;
 }
 g = g->next;
 }

 LinkedList<Room> newRooms;
 Node<Room>* cur = rooms.getHead();
 bool found = false;
 while (cur != nullptr) {
 if (cur->data.maPhong != mp) {
 newRooms.addTail(cur->data);
 } else {
 found = true;
 }
 cur = cur->next;
 }
 rooms = newRooms;
 if (found) cout << " >> Da xoa phong " << mp << "!\n";
 else cout << " >> Khong tim thay!\n";
 }

 // ==================== KHACH ====================
 void themKhach() {
 cout << "\n--- THEM KHACH MOI ---\n";
 string mk = nhapString(" Ma khach: ");
 Node<Guest>* cur = guests.getHead();
 while (cur != nullptr) {
 if (cur->data.maKhach == mk) {
 cout << " >> Loi: Ma khach da ton tai!\n";
 return;
 }
 cur = cur->next;
 }
 string ht = chuanHoaTen(nhapString(" Ho ten: "));
 string cm = nhapString(" CMND/CCCD: ");
 string mpt = nhapString(" Ma phong thue: ");
 // Kiem tra phong ton tai
 bool phongOK = false;
 Node<Room>* r = rooms.getHead();
 while (r != nullptr) {
 if (r->data.maPhong == mpt) { phongOK = true; break; }
 r = r->next;
 }
 if (!phongOK) {
 cout << " >> Loi: Ma phong " << mpt << " khong ton tai!\n";
 return;
 }
 int sd = nhapInt(" So dem o: ", 1, 365);
 string nd = nhapString(" Ngay den (dd/mm/yyyy): ");

 Guest g(mk, ht, cm, mpt, sd, nd);
 guests.addTail(g);

 // Cap nhat trang thai phong
 r = rooms.getHead();
 while (r != nullptr) {
 if (r->data.maPhong == mpt) { r->data.tinhTrang = 1; break; }
 r = r->next;
 }
 cout << " >> Da them khach " << mk << " thanh cong!\n";
 }

 void inDSKhach() {
 if (guests.isEmpty()) {
 cout << "\n>> Danh sach khach rong!\n";
 return;
 }
 cout << "\n==================== DANH SACH KHACH ====================\n";
 cout << left << setw(10) << "Ma KH" << " | "
 << setw(22) << "Ho ten" << " | "
 << setw(14) << "CMND" << " | "
 << setw(10) << "Ma phong" << " | "
 << setw(6) << "So dem" << " | "
 << setw(12) << "Ngay den" << "\n";
 cout << string(80, '-') << "\n";

 Node<Guest>* cur = guests.getHead();
 while (cur != nullptr) {
 cout << left << setw(10) << cur->data.maKhach << " | "
 << setw(22) << cur->data.hoTen << " | "
 << setw(14) << cur->data.cmnd << " | "
 << setw(10) << cur->data.maPhongThue << " | "
 << setw(6) << cur->data.soDem << " | "
 << setw(12) << cur->data.ngayDen << "\n";
 cur = cur->next;
 }
 cout << string(80, '-') << "\n";
 cout << "Tong: " << guests.size() << " khach\n";
 }

 void timKhachTheoCMND() {
 string cm = nhapString(" Nhap CMND: ");
 Node<Guest>* cur = guests.getHead();
 while (cur != nullptr) {
 if (cur->data.cmnd == cm) {
 cout << " Tim thay: " << cur->data.maKhach
 << " - " << cur->data.hoTen
 << " - Phong: " << cur->data.maPhongThue
 << " - " << cur->data.soDem << " dem\n";
 return;
 }
 cur = cur->next;
 }
 cout << " >> Khong tim thay!\n";
 }

 void timKhachTheoTen() {
 string ten = nhapString(" Nhap ten: ");
 bool found = false;
 Node<Guest>* cur = guests.getHead();
 while (cur != nullptr) {
 if (cur->data.hoTen.find(ten) != string::npos) {
 cout << " " << cur->data.maKhach << " - "
 << cur->data.hoTen << " - "
 << cur->data.cmnd << " - Phong: "
 << cur->data.maPhongThue << "\n";
 found = true;
 }
 cur = cur->next;
 }
 if (!found) cout << " >> Khong tim thay!\n";
 }

 void suaKhach() {
 string mk = nhapString(" Nhap ma khach can sua: ");
 Node<Guest>* cur = guests.getHead();
 while (cur != nullptr) {
 if (cur->data.maKhach == mk) {
 cout << " Dang sua khach " << mk << ":\n";
 cur->data.hoTen = chuanHoaTen(nhapString(" Ho ten moi: "));
 cur->data.cmnd = nhapString(" CMND moi: ");
 cur->data.soDem = nhapInt(" So dem moi: ", 1, 365);
 cur->data.ngayDen = nhapString(" Ngay den moi: ");
 cout << " >> Da sua khach " << mk << "!\n";
 return;
 }
 cur = cur->next;
 }
 cout << " >> Khong tim thay!\n";
 }

 void xoaKhach() {
 string mk = nhapString(" Nhap ma khach can xoa: ");
 LinkedList<Guest> newGuests;
 Node<Guest>* cur = guests.getHead();
 string mpt = "";
 bool found = false;
 while (cur != nullptr) {
 if (cur->data.maKhach != mk) {
 newGuests.addTail(cur->data);
 } else {
 mpt = cur->data.maPhongThue;
 found = true;
 }
 cur = cur->next;
 }
 guests = newGuests;
 if (found) {
 // Cap nhat trang thai phong ve trong
 Node<Room>* r = rooms.getHead();
 while (r != nullptr) {
 if (r->data.maPhong == mpt) { r->data.tinhTrang = 0; break; }
 r = r->next;
 }
 cout << " >> Da xoa khach " << mk << "!\n";
 } else {
 cout << " >> Khong tim thay!\n";
 }
 }

 // ==================== SAP XEP ====================
 void sapXepPhongGiaTang() {
 rooms.sort(compareGiaTang);
 cout << "Da sap xep phong theo gia tang dan.\n";
 inDSPhong();
 }

 void sapXepPhongGiaGiam() {
 rooms.sort(compareGiaGiam);
 cout << "Da sap xep phong theo gia giam dan.\n";
 inDSPhong();
 }

 void sapXepPhongTheoMa() {
 rooms.sort(compareMaPhong);
 cout << "Da sap xep phong theo ma.\n";
 inDSPhong();
 }

 void sapXepKhachTheoTen() {
 guests.sort(compareTenKhach);
 cout << "Da sap xep khach theo ten A-Z.\n";
 inDSKhach();
 }

 // ==================== MAX/MIN ====================
 void phongGiaCaoNhat() {
 auto better = [](Room a, Room b) { return a.giaThue > b.giaThue; };
 Node<Room>* best = rooms.findMax(better);
 if (!best) { cout << "Khong co phong!\n"; return; }
 cout << "\n=== PHONG GIA CAO NHAT (" << best->data.giaThue << " VND) ===\n";
 cout << best->data.maPhong << " - " << best->data.loaiPhong
 << " - " << (best->data.tinhTrang == 0 ? "Trong" : "Co khach") << "\n";
 }

 void phongGiaThapNhat() {
 auto worse = [](Room a, Room b) { return a.giaThue < b.giaThue; };
 Node<Room>* best = rooms.findMax(worse);
 if (!best) { cout << "Khong co phong!\n"; return; }
 cout << "\n=== PHONG GIA THAP NHAT (" << best->data.giaThue << " VND) ===\n";
 cout << best->data.maPhong << " - " << best->data.loaiPhong << "\n";
 }

 void khachOLauNhat() {
 auto better = [](Guest a, Guest b) { return a.soDem > b.soDem; };
 Node<Guest>* best = guests.findMax(better);
 if (!best) { cout << "Khong co khach!\n"; return; }
 cout << "\n=== KHACH O LAU NHAT (" << best->data.soDem << " dem) ===\n";
 cout << best->data.maKhach << " - " << best->data.hoTen
 << " - Phong: " << best->data.maPhongThue << "\n";
 }

 void khachMoiNhat() {
 // Khach moi nhat = khach dau tien trong ds (them sau cung)
 Node<Guest>* cur = guests.getHead();
 if (!cur) { cout << "Khong co khach!\n"; return; }
 cout << "\n=== KHACH MOI NHAT ===\n";
 cout << cur->data.maKhach << " - " << cur->data.hoTen
 << " - " << cur->data.ngayDen << "\n";
 }

 // ==================== THONG KE ====================
 void thongKe() {
 int tPhong = rooms.size();
 int tKhach = guests.size();
 int dThue = 0, tTrong = 0;
 double doanhThu = 0;
 int dDon = 0, dDoi = 0, dVip = 0;

 Node<Room>* r = rooms.getHead();
 while (r != nullptr) {
 if (r->data.tinhTrang == 1) dThue++; else tTrong++;
 string lp = r->data.loaiPhong;
 transform(lp.begin(), lp.end(), lp.begin(), ::tolower);
 if (lp == "don" || lp.find("don") != string::npos) dDon++;
 else if (lp == "doi" || lp.find("doi") != string::npos) dDoi++;
 else if (lp == "vip" || lp.find("vip") != string::npos) dVip++;
 r = r->next;
 }

 Node<Guest>* g = guests.getHead();
 while (g != nullptr) {
 r = rooms.getHead();
 while (r != nullptr) {
 if (r->data.maPhong == g->data.maPhongThue) {
 doanhThu += g->data.soDem * r->data.giaThue * r->data.thueSuat / 100.0;
 break;
 }
 r = r->next;
 }
 g = g->next;
 }

 cout << "\n========== THONG KE ==========\n";
 cout << " Tong so phong: " << tPhong << "\n";
 cout << " Phong dang thue: " << dThue << "\n";
 cout << " Phong trong: " << tTrong << "\n";
 cout << " Phong loai Don: " << dDon << "\n";
 cout << " Phong loai Doi: " << dDoi << "\n";
 cout << " Phong loai VIP: " << dVip << "\n";
 cout << " Tong so khach: " << tKhach << "\n";
 cout << " Tong doanh thu thue: " << fixed << setprecision(0) << doanhThu << " VND\n";
 cout << "==============================\n";
 }

 // ==================== MENU ====================
 void hienThiMenu() {
 cout << "\n";
 cout << "+====================== QUAN LY THUE PHONG KHACH SAN ======================+\n";
 cout << "| 1. Quan ly Phong 2. Quan ly Khach 3. Sap xep |\n";
 cout << "| 4. Tim Max/Min 5. Thong ke 6. Luu file |\n";
 cout << "| 7. Doc file 0. Thoat |\n";
 cout << "+===========================================================================+\n";
 cout << "Chon: ";
 }

 void menuPhong() {
 int chon;
 do {
 cout << "\n--- QUAN LY PHONG ---\n";
 cout << "1.Them 2.Hien thi 3.Tim theo ma 4.Tim theo loai\n";
 cout << "5.Sua 6.Xoa 7.In phong thu k 0.Quay lai\nChon: ";
 cin >> chon;
 cin.ignore(numeric_limits<streamsize>::max(), '\n');
 switch (chon) {
 case 1: themPhong(); break;
 case 2: inDSPhong(); break;
 case 3: timPhongTheoMa(); break;
 case 4: timPhongTheoLoai(); break;
 case 5: suaPhong(); break;
 case 6: xoaPhong2(); break;
 case 7: inPhongThuK(); break;
 case 0: break;
 default: cout << "Chon sai!\n";
 }
 } while (chon != 0);
 }

 void menuKhach() {
 int chon;
 do {
 cout << "\n--- QUAN LY KHACH ---\n";
 cout << "1.Them 2.Hien thi 3.Tim theo CMND 4.Tim theo ten\n";
 cout << "5.Sua 6.Xoa 7.In khach thu k 0.Quay lai\nChon: ";
 cin >> chon;
 cin.ignore(numeric_limits<streamsize>::max(), '\n');
 switch (chon) {
 case 1: themKhach(); break;
 case 2: inDSKhach(); break;
 case 3: timKhachTheoCMND(); break;
 case 4: timKhachTheoTen(); break;
 case 5: suaKhach(); break;
 case 6: xoaKhach(); break;
 case 7: inKhachThuK(); break;
 case 0: break;
 default: cout << "Chon sai!\n";
 }
 } while (chon != 0);
}

 void menuSapXep() {
 int chon;
 do {
 cout << "\n--- SAP XEP ---\n";
 cout << "1.Phong gia tang 2.Phong gia giam 3.Phong theo ma 4.Khach theo ten\n0.Quay lai\nChon: ";
 cin >> chon;
 cin.ignore(numeric_limits<streamsize>::max(), '\n');
 switch (chon) {
 case 1: sapXepPhongGiaTang(); break;
 case 2: sapXepPhongGiaGiam(); break;
 case 3: sapXepPhongTheoMa(); break;
 case 4: sapXepKhachTheoTen(); break;
 case 0: break;
 default: cout << "Chon sai!\n";
 }
 } while (chon != 0);
 }

 void menuMaxMin() {
 int chon;
 do {
 cout << "\n--- TIM MAX/MIN ---\n";
 cout << "1.Phong gia cao nhat 2.Phong gia thap nhat\n";
 cout << "3.Khach o lau nhat 4.Khach moi nhat\n0.Quay lai\nChon: ";
 cin >> chon;
 cin.ignore(numeric_limits<streamsize>::max(), '\n');
 switch (chon) {
 case 1: phongGiaCaoNhat(); break;
 case 2: phongGiaThapNhat(); break;
 case 3: khachOLauNhat(); break;
 case 4: khachMoiNhat(); break;
 case 0: break;
 default: cout << "Chon sai!\n";
 }
 } while (chon != 0);
 }

 // ==================== CAU 3: IN PHAN TU THU K ====================
 // Yeu cau: In thong tin cua phan tu thu k tu dau danh sach
 // Input: k nguyen duong (1 <= k <= so luong phan tu)
 // Thuan toan: Duyet tu dau den vi tri thu k (1-indexed)
 // Do phuc tap: O(k)
 void inPhongThuK() {
 int k = nhapInt(" Nhap k: ", 1, rooms.size());
 Node<Room>* cur = rooms.getHead();
 for (int i = 1; i < k; i++) {
 cur = cur->next;
 }
 cout << "\n=== PHONG THU " << k << " ===\n";
 cout << " Ma phong: " << cur->data.maPhong << "\n";
 cout << " Loai phong: " << cur->data.loaiPhong << "\n";
 cout << " Gia thue: " << cur->data.giaThue << " VND\n";
 cout << " Tinh trang: " << (cur->data.tinhTrang == 0 ? "Trong" : "Co khach") << "\n";
 cout << " Thue suat: " << cur->data.thueSuat << " %\n";
 }

 void inKhachThuK() {
 int k = nhapInt(" Nhap k: ", 1, guests.size());
 Node<Guest>* cur = guests.getHead();
 for (int i = 1; i < k; i++) {
 cur = cur->next;
 }
 cout << "\n=== KHACH THU " << k << " ===\n";
 cout << " Ma khach: " << cur->data.maKhach << "\n";
 cout << " Ho ten: " << cur->data.hoTen << "\n";
 cout << " CMND: " << cur->data.cmnd << "\n";
 cout << " Ma phong thue: " << cur->data.maPhongThue << "\n";
 cout << " So dem o: " << cur->data.soDem << "\n";
 cout << " Ngay den: " << cur->data.ngayDen << "\n";
 }

 void run() {
 int chon;
 do {
 hienThiMenu();
 cin >> chon;
 cin.ignore(numeric_limits<streamsize>::max(), '\n');
 switch (chon) {
 case 1: menuPhong(); break;
 case 2: menuKhach(); break;
 case 3: menuSapXep(); break;
 case 4: menuMaxMin(); break;
 case 5: thongKe(); break;
 case 6: luuFile(); break;
 case 7: docFile(); break;
 case 0:
 ghiFileTuDong();
 cout << "Cam on da su dung chuong trinh!\n";
 break;
 default:
 cout << "Chon sai! Vui long nhap lai.\n";
 }
 } while (chon != 0);
 }
};

int main() {
 try {
 HotelManager manager;
 manager.run();
 } catch (const exception &e) {
 cerr << "Loi: " << e.what() << endl;
 return 1;
 }
 return 0;
}
