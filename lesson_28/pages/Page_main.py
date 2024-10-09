from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By



class Main_page:
    def __init__(self, driver):
        self.driver = driver

    def sing_up_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'button.hero-descriptor_btn.btn.btn-primary')





