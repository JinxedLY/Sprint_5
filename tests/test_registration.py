from conftest import driver
from pathways import Pathways
from locators import RegLocator, LoginLocator
from test_data import rand_mocky
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestingRegistration:

    def test_registration_random_valid_data_success(self, driver):
        driver.get(Pathways.reg_path)
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(RegLocator.reg_button))
        driver.find_element(*RegLocator.name_field).send_keys(rand_mocky.username)
        driver.find_element(*RegLocator.email_field).send_keys(rand_mocky.email)
        driver.find_element(*RegLocator.pass_field).send_keys(rand_mocky.password)
        driver.find_element(*RegLocator.reg_button).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(LoginLocator.login_button))

        assert driver.current_url == Pathways.login_path

    def test_registration_invalid_password_error(self, driver):
        driver.get(Pathways.reg_path)
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(RegLocator.reg_button))
        driver.find_element(*RegLocator.name_field).send_keys(rand_mocky.username)
        driver.find_element(*RegLocator.email_field).send_keys(rand_mocky.email)
        driver.find_element(*RegLocator.pass_field).send_keys(rand_mocky.incorrect_password)
        driver.find_element(*RegLocator.reg_button).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(RegLocator.pass_error))
        error_message = driver.find_element(*RegLocator.pass_error).text

        assert error_message == "Некорректный пароль"
