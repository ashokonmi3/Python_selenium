from selenium import webdriver

from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.whatarecookies.com/")
elem=driver.find_element_by_tag_name('html')
elem.send_keys(Keys.END)
sleep(5)
elem.send_keys(Keys.HOME)
sleep(5)

driver.quit()

