import time
from selenium.webdriver.common.by import By
from utils.wait import get_frame
from utils.browser import load_extension_page

def tai_meovoi(driver, masothue, matracu, url):
    load_extension_page(driver, url)
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "txtCode").send_keys(matracu)
    driver.find_element(By.ID, "btnSearchInvoice").click()
    time.sleep(5)

    kiemtra = get_frame(driver, url)
    if kiemtra:
        print("Hóa đơn có hiệu lực")
        driver.execute_script("""
            document
                .evaluate("//div[contains(text(), 'Tải hóa đơn dạng XML')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null)
                .singleNodeValue
                .click();
        """)
        load_extension_page(driver, kiemtra)
        time.sleep(2)
