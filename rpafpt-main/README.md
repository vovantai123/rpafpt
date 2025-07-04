# 🧾 RPA FPT – Tải Hóa Đơn XML Tự Động

Tool hỗ trợ tự động tra cứu và tải hóa đơn điện tử từ các trang như FPT, MInvoice, eHoadon...  
Sử dụng `Selenium + ChromeDriver`, hỗ trợ nhiều loại hóa đơn, lưu kết quả về Excel.

---

## 🚀 Cách sử dụng

### 1. Chuẩn bị
- Cài Python 3.9+ (nên dùng Python 64-bit)
- Cài các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

### 2. Chuẩn bị file `input.xlsx`
- Tạo file `input.xlsx` với các cột:
  - `Mã số thuế`
  - `Mã tra cứu`
  - `URL` (link trang tra cứu hóa đơn)

### 3. Cấu hình đường dẫn tải
- Tạo file `duongdantai.txt`, ghi đường dẫn thư mục bạn muốn lưu XML, ví dụ:
```
E:\toolthaotac\RegUnlock-Instagram\RegUnlock-Instagram\fpt
```

- Tạo file `profiletamthoi.txt`, ví dụ:
```
E:\toolthaotac\RegUnlock-Instagram\RegUnlock-Instagram\fpt\profiletam
```

### 4. Chạy chương trình
```bash
python main.py
```

---

## 📁 Cấu trúc thư mục

```
rpafpt/
├── main.py
├── core.py
├── input.xlsx
├── duongdantai.txt
├── profiletamthoi.txt
├── handlers/
│   ├── fpt.py
│   ├── meinvoice.py
│   └── ehoadon.py
├── utils/
│   ├── browser.py
│   └── invoice_xml.py
├── output.xlsx
```

---

## 📦 Build file .exe (tuỳ chọn)
Dành cho người dùng không cài Python:

```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

File `.exe` sẽ nằm trong thư mục `dist/`

