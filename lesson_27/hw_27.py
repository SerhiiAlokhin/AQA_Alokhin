from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Ініціалізація веб-драйвера для Chrome
driver = webdriver.Chrome()
driver.get("https://tracking.novaposhta.ua/#/uk")
sleep(2)
search_field = driver.find_element(By.XPATH, "//input[contains(@class, 'track__form-group-input')]")
button =driver.find_element(By.ID,"np-number-input-desktop-btn-search-en" ) #'//*[@id="np-number-input-desktop-btn-search-en"]'

def test_check_track_num():
    search_field.send_keys('59001216334608')
    button.click()
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "chat"), "Отримана"))
