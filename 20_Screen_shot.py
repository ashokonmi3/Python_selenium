import os
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.python.org")
# os.chdir("C:\My\Study\Python_Selenium\Program")
driver.get_screenshot_as_file('foo1.png')
driver.quit()

