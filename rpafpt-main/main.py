from handlers import fpt, meinvoice, ehoadon
from utils.browser import start_chrome
from utils.invoice_xml import xulyxml
import pandas as pd
import os
import shutil
handlers = {
    'fpt': fpt.tai_fpt,
    'meinvoice': meinvoice.tai_meovoi,
    'ehoadon': ehoadon.ehodon,
}

def get_handler(url):
    for key in handlers:
        if key in url.lower():
            return handlers[key]
    return None

if __name__ == '__main__':
    df = pd.read_excel("input.xlsx", dtype={"Mã số thuế": str})
    for index, row in df.iterrows():
        masothue = row['Mã số thuế']
        matracu = row['Mã tra cứu']
        url = row['URL']

        driver, taixuong, profile_path = start_chrome(matracu)
        handler = get_handler(url)

        if handler:
            handler(driver, masothue, matracu, url)
            xulyxml(taixuong, masothue, matracu, url)
        else:
            print(f"Không tìm thấy hàm xử lý phù hợp cho URL: {url}")

        driver.quit()
        if os.path.exists(profile_path):
            parent_dir = os.path.dirname(profile_path)
            try:
                shutil.rmtree(parent_dir)
                print(f"✅ Đã xóa thư mục tạm: {parent_dir}")
            except Exception as e:
                print(f"⚠️ Không thể xóa thư mục {parent_dir}: {e}")
