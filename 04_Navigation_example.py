import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.implicitly_wait(15)

driver.get("http://www.python.org")

elem = driver.find_element_by_link_text("Community")
sleep(5)
elem.click()
sleep(5)
driver.back()
sleep(5)
driver.forward()
#driver.execute_script("window.history.go(-1)")
# driver.navigate().back()
# elem.send_keys("viswa")
# elem.send_keys(Keys.RETURN)
# 
driver.quit()
