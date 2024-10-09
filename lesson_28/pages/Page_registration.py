from selenium.webdriver.common.by import By



class Registration_page:
    def __init__(self, driver):
        self.driver = driver

    def registration_window(self):
        return self.driver.find_element(By.XPATH, "//h4[text()='Registration']")

    def name_field(self):
        return self.driver.find_element(By.ID, "signupName")

    def last_name_field(self):
        return self.driver.find_element(By.ID, "signupLastName")

    def email_field(self):
        return self.driver.find_element(By.ID, "signupEmail")

    def password_field(self):
        return self.driver.find_element(By.ID, 'signupPassword')

    def repeat_password_field(self):
        return self.driver.find_element(By.ID, 'signupRepeatPassword')

    def registration_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary[disabled]')