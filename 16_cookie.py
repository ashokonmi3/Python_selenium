from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import re
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://bing.com")
# print (driver.get_cookies())

driver.add_cookie({"name": "foo", "value": "bar"})

# get browser cookie
print(driver.get_cookie("foo"))

# get all cookies in scope of session
print(driver.get_cookies())

# delete browser cookie
driver.delete_cookie("foo")

# clear all cookies in scope of session
driver.delete_all_cookies()

driver.close()