from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://google.com")
sleep(3)
body=driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'t')
sleep(5)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'w')
sleep(5)

driver.quit()


# ====
# color and keys needs to be checked