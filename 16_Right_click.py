from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://google.com/")
# driver.get("https://google.com")
element=driver.find_element_by_xpath("//input[@value='Google Search']")
click=ActionChains(driver).context_click(element)
click.perform()
sleep(5)
driver.quit()
