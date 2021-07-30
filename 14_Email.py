from selenium import webdriver
from time import sleep
import re

driver = webdriver.Chrome()
driver.get("http://www.airindia.in/customer-support.htm")
doc= driver.page_source
emails=re.findall(r'[\w\.-]+@[\w\.-]+',doc)
for email in emails:
	print (email)
print(f"Total email address present is {len(email)}")

sleep(3)
driver.close()
