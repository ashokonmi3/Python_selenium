from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# driver = webdriver.Ie()
driver = webdriver.Chrome()

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
sleep(5)
elem.clear()
elem.send_keys("biocon")
sleep(5)
elem.send_keys(Keys.RETURN)
# it is for  press enter key
assert "No results found." in driver.page_source
sleep(5)

driver.quit()
