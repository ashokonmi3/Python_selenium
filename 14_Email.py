from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import re
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.airindia.in/customer-support.htm")
doc= driver.page_source
emails=re.findall(r'[\w\.-]+@[\w\.-]+',doc)

for email in emails:
	print email

sleep(3)
driver.close()
