import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import sleep
import warnings
import urllib3


class GoogleSeachTest(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def test_GoogleSearch(self):
        driver_chrome = webdriver.Chrome()
        self.driver = driver_chrome
        driver_chrome.maximize_window()
        driver_chrome.get('http://www.google.com')

        # Perform search operation
        elem = driver_chrome.find_element(By.NAME, "q")
        elem.send_keys("python")
        elem.submit()

    def tearDown(self):
        # Close the browser.
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()