from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import re
driver = webdriver.Chrome()
# driver.maximize_window()
driver.get("http://www.airindia.in/customer-support.htm")
doc= driver.page_source
#numbers=re.findall(r'[(][\d]{3}[)][]?[\d]{3}-[\d]{4}',doc)
numbers=re.findall(r'[\d]{8}',doc)

print numbers
# for number in numbers:
# 	print number

