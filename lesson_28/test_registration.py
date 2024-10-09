import allure
import pytest
from faker import Faker

fake = Faker()
password = fake.password()


@allure.feature('Registration')
def test_registration(driver, open_main_page,start_registration,registration,check_that_registration_has_done):
    open_main_page()
    start_registration()
    registration(fake.first_name(),fake.last_name(),fake.email(),password)
    assert check_that_registration_has_done(), "Registration failed"
