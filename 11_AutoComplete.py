
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

# driver = webdriver.Ie()
driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://jqueryui.com/autocomplete")
frame=driver.find_element_by_tag_name("iframe")
driver.switch_to_frame(frame)
inputfield=driver.find_element_by_xpath("//input[@id='tags']")
sleep(3)
inputfield.send_keys('ja')
sleep(10)

message=driver.find_element_by_xpath("//div[contains(.,'JavaScript')]")

message.click()
sleep(10)
driver.quit()


