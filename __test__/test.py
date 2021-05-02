
import drivers.web_driver as drivers
import scenarios.basic as basic
import os
import sys
import requests
import unittest
from webdriver_manager.chrome import ChromeDriverManager
import selenium
sys.path.append(os.path.abspath(".."))


class test_selenium(unittest.TestCase):
    def setUp(self):
        self.driver = drivers.getDriver()

    def test_show_page(self):
        execute_scenario(self.driver, self.show_page)

    def show_page(self):
        driver = self.driver
        basic.show_page(driver)
        header = driver.find_element_by_xpath('//*[@id="root"]')
        self.assertIsNotNone(header)

    def test_show_logout_button(self):
        execute_scenario(self.driver, self.show_logout_button)

    def show_logout_button(self):
        driver = self.driver

        basic.show_page(driver)
        is_exist_logout_button = is_missing_element(driver,
                                                    '//*[@id="menu-appbar"]/div[3]/ul/li')

        self.assertFalse(is_exist_logout_button, "Logout Button is not exist")

        basic.click_account_icon(driver)
        logoutButton = driver.find_element_by_xpath(
            '//*[@id="menu-appbar"]/div[3]/ul/li')
        self.assertTrue(logoutButton.is_enabled())

    def tearDown(self):
        self.driver.close()


def execute_scenario(driver, fn):
    try:
        fn()
    except Exception as e:
        print("Exception in test: ", e)
        driver.get_screenshot_as_file('screens/ss-%s.png' % fn.__name__)
        raise e


def is_missing_element(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except selenium.common.exceptions.NoSuchElementException as err:
        return False
    else:
        print(arg, 'has', len(f.readlines()), 'lines')


if __name__ == "__main__":
    unittest.main()
