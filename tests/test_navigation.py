from conftest import driver, mocky_auth_driver
from pathways import Pathways
from locators import LoginLocator, MainLocator, DashLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestingNavigation:
    def test_navigation_to_dash_success(self, driver, mocky_auth_driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainLocator.post_order))
        driver.find_element(*MainLocator.dash_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(DashLocator.logout_button))

        assert driver.current_url == Pathways.dash_path

    def test_navigation_from_dash_to_constructor_success(self, driver, mocky_auth_driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainLocator.post_order))
        driver.get(Pathways.dash_path)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(DashLocator.logout_button))
        driver.find_element(*DashLocator.constructor_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainLocator.post_order))

        assert driver.current_url == Pathways.base_path

    def test_navigation_from_dash_to_main_via_logo_success(self, driver, mocky_auth_driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainLocator.post_order))
        driver.get(Pathways.dash_path)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(DashLocator.logout_button))
        driver.find_element(*DashLocator.logo_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainLocator.post_order))

        assert driver.current_url == Pathways.base_path

    def test_navigation_from_dash_logout_button_logout(self, driver, mocky_auth_driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainLocator.post_order))
        driver.get(Pathways.dash_path)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(DashLocator.logout_button))
        driver.find_element(*DashLocator.logout_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginLocator.login_button))

        assert driver.current_url == Pathways.login_path

    def test_navigation_category_bun_success(self, driver):
        driver.get(Pathways.base_path)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainLocator.login_button))
        driver.find_element(*MainLocator.sauce_tab).click()
        driver.find_element(*MainLocator.buns_tab).click()
        active_tab_text = driver.find_element(*MainLocator.active_tab).text
        assert active_tab_text == 'Булки'

    def test_navigation_category_sauce_success(self, driver):
        driver.get(Pathways.base_path)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainLocator.login_button))
        driver.find_element(*MainLocator.sauce_tab).click()
        active_tab_text = driver.find_element(*MainLocator.active_tab).text
        assert active_tab_text == 'Соусы'

    def test_navigation_category_fillings_success(self, driver):
        driver.get(Pathways.base_path)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainLocator.login_button))
        driver.find_element(*MainLocator.fillings_tab).click()
        active_tab_text = driver.find_element(*MainLocator.active_tab).text
        assert active_tab_text == 'Начинки'
