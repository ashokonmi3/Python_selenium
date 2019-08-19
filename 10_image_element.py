from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.wikipedia.org/")
element=driver.find_element_by_class_name("central-featured-logo")

# element=driver.find_element_by_tag_name('img')
# //*[@id="www-wikipedia-org"]/div[1]
print element.tag_name
print element.size
print element.location
driver.quit()