import pandas as pd
from handlers import fpt, meinvoice, ehoadon
from utils.browser import start_chrome
from utils.invoice_xml import xulyxml
import shutil
import os
handlers = {
    'fpt': fpt.tai_fpt,
    'meinvoice': meinvoice.tai_meovoi,
    'ehoadon': ehoadon.ehodon
}

def get_handler(url):
    for key in handlers:
        if key in url.lower():
            return handlers[key]
    return None

def run_main():
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
                shutil.rmtree(os.path.dirname(profile_path), ignore_errors=True)
                print(f"🧹 Đã xóa thư mục tạm profile: {profile_path}")