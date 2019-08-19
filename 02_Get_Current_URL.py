from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.zkoss.org/zkdemo/input/radio_button")
# driver.get("https://google.com")
current_url=driver.current_url
print (driver.current_url)
sleep(5)


# driver.get("https://www.zkoss.org/zkdemo/input/radio_button")
# driver.get("https://google.com")
# current_url=driver.current_url
# print (driver.current_url)



sleep(5)
driver.quit()



