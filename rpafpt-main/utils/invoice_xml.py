import os
import xml.etree.ElementTree as ET
from utils.excel import ghi_vao_excel_pandas

def extract_invoice_fields(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    def find_text(path):
        el = root.find(path)
        return el.text.strip() if el is not None and el.text else ""
    return {
        "so_hoa_don": find_text(".//SHDon"),
        "ten_nguoi_ban": find_text(".//NBan/Ten"),
        "mst_nguoi_ban": find_text(".//NBan/MST"),
        "dia_chi_ban": find_text(".//NBan/DChi"),
        "so_tai_khoan_ban": find_text(".//NBan/STKNHang"),
        "ten_nguoi_mua": find_text(".//NMua/Ten"),
        "dia_chi_mua": find_text(".//NMua/DChi"),
        "mst_nguoi_mua": find_text(".//NMua/MST"),
    }

def xulyxml(taixuong, masothue, matracu, url):
    xml_file = next((f for f in os.listdir(taixuong) if f.lower().endswith(".xml")), None)
    if xml_file:
        xml_path = os.path.join(taixuong, xml_file)
        try:
            data = extract_invoice_fields(xml_path)
        except Exception as e:
            print(f"Lỗi đọc XML: {e}")
            data = {}
    else:
        print("Không có file XML")
        data = {}

    final_data = {
        "Mã số thuế": masothue,
        "Mã tra cứu": matracu,
        "URL": url,
        **data
    }
    ghi_vao_excel_pandas(final_data)
