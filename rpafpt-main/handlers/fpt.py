from urllib.parse import urlparse
import time
from selenium.webdriver.common.by import By
from utils.wait import get_frame
from utils.browser import load_extension_page

def tai_fpt(driver, masothue, matracu, url):
    load_extension_page(driver, url)
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@placeholder='MST bên bán']").send_keys(masothue)
    driver.find_element(By.XPATH, "//input[@placeholder='Mã tra cứu hóa đơn']").send_keys(matracu)
    driver.find_element(By.XPATH, "//button[normalize-space(text())='Tra cứu']").click()
    time.sleep(5)

    parsed = urlparse(url)
    target_src = f"{parsed.scheme}://{parsed.netloc}"
    kiem_tra = get_frame(driver, target_src)
    if kiem_tra:
        print("Hóa đơn có hiệu lực")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space(text())='Tải XML']").click()
        load_extension_page(driver, kiem_tra)
        time.sleep(2)
