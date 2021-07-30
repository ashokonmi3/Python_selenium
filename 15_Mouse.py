from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://google.com/")
element=driver.find_element_by_link_text("Gmail")
action_hover=ActionChains(driver)
hover=action_hover.move_to_element(element)
sleep(1)
hover.click()
hover.perform()
sleep(5)
driver.quit()
