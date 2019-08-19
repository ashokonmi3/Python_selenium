from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
# driver.maximize_window()
driver.get("https://www.zkoss.org/zkdemo/input/radio_button")
# driver.get("https://google.com")
for i in driver.find_elements_by_xpath("//*[@type='radio']"):
	i.click()
	sleep(2)



sleep(5)
driver.quit()



