from conftest import driver
from pathways import Pathways
from locators import RegLocator, LoginLocator, MainLocator, RecoveryLocator
from test_data import mocky
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestingLogin:

    def test_login_from_login_button_success(self, driver):
        driver.get(Pathways.base_path)
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(MainLocator.login_button))
        driver.find_element(*MainLocator.login_button).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(LoginLocator.login_button))
        driver.find_element(*LoginLocator.email_field).send_keys(mocky.email)
        driver.find_element(*LoginLocator.pass_field).send_keys(mocky.password)
        driver.find_element(*LoginLocator.login_button).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(MainLocator.post_order))

        assert driver.current_url == Pathways.base_path

    def test_login_from_dashboard_button_success(self, driver):
        driver.get(Pathways.base_path)
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(MainLocator.login_button))
        driver.find_element(*MainLocator.dash_button).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(LoginLocator.login_button))
        driver.find_element(*LoginLocator.email_field).send_keys(mocky.email)
        driver.find_element(*LoginLocator.pass_field).send_keys(mocky.password)
        driver.find_element(*LoginLocator.login_button).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(MainLocator.post_order))

        assert driver.current_url == Pathways.base_path

    def test_login_from_registration_page_success(self, driver):
        driver.get(Pathways.reg_path)
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(RegLocator.login_redirect))
        driver.find_element(*RegLocator.login_redirect).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(LoginLocator.login_button))
        driver.find_element(*LoginLocator.email_field).send_keys(mocky.email)
        driver.find_element(*LoginLocator.pass_field).send_keys(mocky.password)
        driver.find_element(*LoginLocator.login_button).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(MainLocator.post_order))

        assert driver.current_url == Pathways.base_path

    def test_login_from_recovery_page_success(self, driver):
        driver.get(Pathways.recover_path)
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(RecoveryLocator.login_redirect))
        driver.find_element(*RecoveryLocator.login_redirect).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(LoginLocator.login_button))
        driver.find_element(*LoginLocator.email_field).send_keys(mocky.email)
        driver.find_element(*LoginLocator.pass_field).send_keys(mocky.password)
        driver.find_element(*LoginLocator.login_button).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(MainLocator.post_order))

        assert driver.current_url == Pathways.base_path
