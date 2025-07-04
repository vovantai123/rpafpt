from selenium.webdriver.common.by import By

def get_frame(driver, target_src):
    driver.implicitly_wait(10)
    iframes = driver.find_elements(By.CSS_SELECTOR, "iframe")
    matched_iframes = []
    for iframe in iframes:
        src = iframe.get_attribute("src")
        if src and target_src in src:
            matched_iframes.append((src, iframe))
    if matched_iframes:
        best_src, best_iframe = max(matched_iframes, key=lambda x: len(x[0]))
        print(f"Chọn iframe: {best_src}")
        return best_src
    else:
        print("Không tìm thấy iframe phù hợp")
        return False
