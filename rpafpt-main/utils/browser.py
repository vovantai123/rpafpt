from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random
def start_chrome(matracu):
    options = Options()
    with open("duongdantai.txt", "r", encoding="utf-8") as f:
        base_dir = f.read().strip()

    # Gắn thêm thư mục theo mã tra cứu
    taixuong = os.path.join(base_dir, matracu)
    os.makedirs(taixuong, exist_ok=True)


    options.add_experimental_option("prefs", {
        "download.default_directory": taixuong,
        "download.prompt_for_download": False,
        "plugins.always_open_pdf_externally": True,
        "safebrowsing.enabled": True,
        "profile.content_settings.exceptions.automatic_downloads.*.setting": 1,
    })
    characters = string.ascii_letters + string.digits
    random_folder_name = ''.join(random.choice(characters) for _ in range(7))
    with open('profiletamthoi.txt', 'r') as file:
        profile = file.read().strip()
    temp_dir = os.path.join(profile, random_folder_name)
    profile_path = os.path.join(temp_dir, "Data/profile")
    options.add_argument('--user-data-dir=' + profile_path)
    options.add_argument("--disable-notifications")
    options.add_argument("--lang=en")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-logging")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = ChromeService(executable_path="chromedriver.exe", options=options)
    driver = webdriver.Chrome(service=service, options=options)
    return driver, taixuong,profile_path

def load_extension_page(driver, url, max_load_time=30, retries=100):
    attempt = 0
    while attempt < retries:
        try:
            driver.set_page_load_timeout(max_load_time)
            driver.get(url)
            WebDriverWait(driver, max_load_time).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )
            print(f"Trang web {url} đã tải xong.")
            break
        except Exception as e:
            print(f"Thử lại {attempt + 1} lần: {e}")
            attempt += 1
            time.sleep(2)
