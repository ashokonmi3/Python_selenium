#Collection of String values
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

source = open("input.txt", "r")
values = source.readlines()
source.close()
# Execute For loop for each String in the values array
# driver = webdriver.Firefox()
driver=webdriver.Chrome()

for search in values:
    # driver = webdriver.Firefox()
    # driver=webdriver.Chrome()
    driver.get('http://www.google.com')
    # element=driver.find_element_by_name("q").send_keys(search)
    # element.send_keys(Keys.RETURN)
    # # element1.click()
    # sleep(5)
    # #element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(., 'Results')]"))
    # #assert search in element.text
    # assert "No Result found." not in driver.page_source
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys(search)
    sleep(2)
    # elem.send_keys(Keys.RETURN)
    # sleep(2)
    assert "No Result found." not in driver.page_source
driver.close()