from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
print(driver.get_window_size())
driver.get("https://google.com")
driver.set_window_size(1024,768)
sleep(3)
print(driver.get_window_size())
driver.maximize_window()
sleep(5)
print(driver.get_window_size())
sleep(5)
driver.close()
# elem=driver.find_element_by_xpath("html/body/form/table[2]/tbody/tr/td[2]/table/tbody/tr[1]/td[1]/table/tbody/tr[3]/td[2]/table/tbody/tr[6]/td[2]")
# elem.click()