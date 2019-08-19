from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://google.com")
driver.set_window_position(150,200)
sleep(3)
print(driver.get_window_position())
sleep(3)

driver.close()