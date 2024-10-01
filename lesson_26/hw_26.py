
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


def check_frame(input, button, secret):
    input.send_keys(secret)
    sleep(2)
    button.click()
    sleep(2)
    alert = Alert(driver)
    assert alert.text == "Верифікація пройшла успішно!"
    sleep(2)
    alert.accept()


# Ініціалізація веб-драйвера для Chrome
driver = webdriver.Chrome()
url = 'http://localhost:8000/dz.html'
# Відкриття веб-сторінки
driver.get(url)

# Робота с першим фреймом
driver.switch_to.frame(driver.find_element(By.ID, "frame1"))
frame1_input = driver.find_element(By.ID,'input1')
frame1_button = driver.find_element(By.XPATH,'/html/body/button')
secret_f1 = 'Frame1_Secret'
#Перевірка 1го фрейму
check_frame(frame1_input,frame1_button,secret_f1)

# Повернення на основний фрейм
driver.switch_to.parent_frame()

#Робота з другим фреймом
driver.switch_to.frame(driver.find_element(By.ID, "frame2"))
frame2_input = driver.find_element(By.ID,'input2')
frame2_button = driver.find_element(By.XPATH,'/html/body/button')
secret_f2 = 'Frame2_Secret'

#Перевірка 2го фрейму
check_frame(frame2_input,frame2_button,secret_f2)

driver.quit()
