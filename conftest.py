import pytest
from selenium import webdriver
from pathways import Pathways
from locators import MainLocator, LoginLocator
from test_data import (mocky)


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def mocky_auth_driver(driver):
    driver.get(Pathways.base_path)
    driver.find_element(*MainLocator.login_button).click()
    driver.find_element(*LoginLocator.email_field).send_keys(mocky.email)
    driver.find_element(*LoginLocator.pass_field).send_keys(mocky.password)
    driver.find_element(*LoginLocator.login_button).click()
