from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://bgp.he.net/")
sleep(5)

body=driver.find_element_by_tag_name('body')
sleep(5)
body.send_keys(Keys.CONTROL+'a')
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'w')
sleep(5)

driver.quit()