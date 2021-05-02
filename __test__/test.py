
import drivers.web_driver as drivers
import scenarios.basic as basic
import os
import sys
import requests
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
sys.path.append(os.path.abspath(".."))


driver = drivers.getDriver()


class test_selenium(unittest.TestCase):
    def setup(self):
        pass

    def test_show_page(self):
        basic.show_page(driver)
        basic.click_account_icon(driver)
        logoutButton = driver.find_element_by_xpath(
            '//*[@id="menu-appbar"]/div[3]/ul/li')
        assert logoutButton.is_enabled()


if __name__ == "__main__":
    unittest.main()
