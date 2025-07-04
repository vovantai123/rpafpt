import time
from selenium.webdriver.common.by import By
from utils.browser import load_extension_page

def ehodon(driver, masothue, matracu, url):
    load_extension_page(driver, url)
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@placeholder='Nhập Mã tra cứu Hóa đơn']").send_keys(matracu)
    driver.find_element(By.XPATH, "//input[@value='Tra cứu']").click()
    time.sleep(5)

    if "Bạn vui lòng thử lại!" in driver.page_source:
        print("Hóa đơn không hợp lệ hoặc không tồn tại.")
        return
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "frameViewInvoice")
    

    js_code = """
    const iframes = document.querySelectorAll("iframe");

    for (const iframe of iframes) {
    try {
        const doc = iframe.contentDocument || iframe.contentWindow.document;
        const elements = doc.querySelectorAll("button, a, .txt-download-xml");

        elements.forEach(el => {
        if (el.textContent.trim().toLowerCase().includes("xml")) {
            el.click();
            console.log("Clicked in iframe:", el);
        }
        });
    } catch (e) {
        console.warn("Không thể truy cập iframe do cross-origin:", iframe.src);
    }
    }
    """
    driver.execute_script(js_code)
    time.sleep(2)
    js_code = """
    const iframes = document.querySelectorAll("iframe");

    for (const iframe of iframes) {
        try {
            const doc = iframe.contentDocument || iframe.contentWindow.document;
            const elements = doc.querySelectorAll("a");

            elements.forEach(el => {
                if (el.textContent.trim().toLowerCase().includes("pdf")) {
                    el.click();
                    console.log("Clicked PDF link in iframe:", el);
                }
            });
        } catch (e) {
            console.warn("Không thể truy cập iframe do cross-origin:", iframe.src);
        }
    }
    """
    driver.execute_script(js_code)
    time.sleep(3)
    time.sleep(2)
