
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/dialog/")
frame=driver.find_element_by_tag_name("iframe")
driver.switch_to_frame(frame)
frame_title=driver.find_element_by_xpath("//span[text()='Basic dialog']")
assert frame_title.text=='Basic dialog'
driver.switch_to_default_content()
sleep(3)
driver.quit()