import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.wikipedia.org/")
dropdown=driver.find_element_by_id("searchLanguage")
select=Select(dropdown)
sleep(3)
select.select_by_visible_text("Dansk")
sleep(3)
select.select_by_value("en")
sleep(3)
select.select_by_index(1)
sleep(3)
driver.close()
