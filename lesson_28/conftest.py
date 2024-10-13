
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AQA_Alokhin.lesson_28.pages.Page_home import Home_page
from AQA_Alokhin.lesson_28.pages.Page_main import Main_page
from AQA_Alokhin.lesson_28.pages.Page_registration import Registration_page

import pytest
import allure


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def open_main_page(driver):
    @allure.step("Відкриваємо сторінку")
    def _open_start_page():
        driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
    return _open_start_page

@pytest.fixture
def start_registration(driver):
    @allure.step("Відкрити вікно реестрації")
    def _start_registration():
        main_page = Main_page(driver)
        sign_up_button = main_page.sing_up_button()
        sign_up_button.click()
    return _start_registration

@pytest.fixture
def registration(driver):
    @allure.step("Вносимо дані")
    def _registration(name, lastname, email, password):
        registration_page = Registration_page(driver)

        name_field = registration_page.name_field()
        lastname_field = registration_page.last_name_field()
        email_field = registration_page.email_field()
        password_field = registration_page.password_field()
        repeat_password_field = registration_page.repeat_password_field()
        reg_button = registration_page.registration_button()

        name_field.send_keys(name)
        lastname_field.send_keys(lastname)
        email_field.send_keys(email)
        password_field.send_keys(password)
        repeat_password_field.send_keys(password)
        reg_button.click()
    return _registration

@pytest.fixture
def check_that_registration_has_done(driver):
    @allure.step("Перевірка реєстраціъ")
    def _check_that_registration_has_done():
        home_page = Home_page(driver)
        reg_result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"a.btn-link.text-danger"))
        )
        return reg_result.is_displayed()
    return _check_that_registration_has_done