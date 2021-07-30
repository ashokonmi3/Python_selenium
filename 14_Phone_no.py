from selenium import webdriver

import re
driver = webdriver.Chrome()
driver.get("http://www.airindia.in/customer-support.htm")
doc= driver.page_source
numbers=re.findall(r'[\d]{8}',doc)

print (numbers)
for number in numbers:
	print (number)
print ("total mobile no are ",len(numbers))
driver.close()