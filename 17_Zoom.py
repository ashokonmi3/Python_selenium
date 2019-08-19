from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://en.wikipedia.org")
sleep(3)
driver.execute_script("document.body.style.zoom='250%'")
sleep(5)
driver.quit()