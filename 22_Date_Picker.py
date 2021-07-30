

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/datepicker/")
# "http://seleniumhq.github.io/selenium/docs/api/java/index.html"

frame=driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(frame)
datepicker=driver.find_element_by_id("datepicker")
datepicker.click()
sleep(3)
day=driver.find_element_by_xpath("//table/tbody/tr/td/a[text()='13']")
day.click()
sleep(3)
datepicker=driver.find_element_by_id("datepicker")
print ("date is " , datepicker.get_attribute('value'))
driver.switch_to.default_content()
driver.quit()
# //*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[2]/a