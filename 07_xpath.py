from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get("https://www.google.co.in/?gfe_rd=cr&dcr=0&ei=HsaFWpWICLLv8we_3JzQCw")
# //*[@id="lst-ib"]
element=driver.find_element_by_xpath("//input[@class='gsfi lst-d-f']")
print element

element.send_keys("biocon")

sleep(5)
# driver.quit()