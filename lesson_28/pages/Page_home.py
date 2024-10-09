from selenium.webdriver.common.by import By

class Home_page:
    def __init__(self, driver):
        self.driver = driver

    def logout_button(self):
        return self.driver.find_element(By.CSS_SELECTOR,"a.btn-link.text-danger")