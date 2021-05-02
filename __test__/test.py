
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
        driver = self.driver
        basic.show_page(driver)
        header = driver.find_element_by_xpath('//*[@id="root"]')
        self.assertIsNotNone(header)

    def test_show_logout_button(self):
        driver = self.driver

        basic.show_page(driver)
        is_exist_logout_button = element_is_missing(driver,
                                                    '//*[@id="menu-appbar"]/div[3]/ul/li')

        self.assertFalse(is_exist_logout_button)

        basic.click_account_icon(driver)
        logoutButton = driver.find_element_by_xpath(
            '//*[@id="menu-appbar"]/div[3]/ul/li')
        self.assertTrue(logoutButton.is_enabled())

    def tearDown(self):
        self.driver.close()


def element_is_missing(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except selenium.common.exceptions.NoSuchElementException as err:
        print("could not find element in xpath ", err)
        return False
    else:
        print(arg, 'has', len(f.readlines()), 'lines')


if __name__ == "__main__":
    unittest.main()
