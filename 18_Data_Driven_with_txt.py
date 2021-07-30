from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

source = open("input.txt", "r")
values = source.readlines()
source.close()
# Execute For loop for each String in the values array
driver=webdriver.Chrome()
driver.get('http://www.google.com')
for search in values:
    elem = driver.find_element_by_name("q")
    print(search)
    elem.clear()
    elem.send_keys(search)
    sleep(2)
    print("pressing back")
    sleep(5)
    driver.back()
driver.close()