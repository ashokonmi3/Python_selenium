from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

# driver = webdriver.Ie()
driver = webdriver.Chrome()

driver.maximize_window()
driver.get("http://www.ksrtc.in/oprs-web/")
# driver.get("https://google.com")
element=driver.find_element_by_name("searchBtn")
sleep(5)
element.click()
sleep(5)
alert=driver.switch_to_alert()
alert.accept()
sleep(15)
driver.quit()
