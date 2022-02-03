from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ashokonmi3.github.io/Selenium.Pages/Practice_handling_Alerts.html")
sleep(5)
element=driver.find_element_by_name("alert")
element.click()
sleep(3)
alert=driver.switch_to.alert
alert_string=alert.text
print(alert_string)
alert.accept()
print(" Selecting the cancel option ")
element=driver.find_element_by_name("confirmation")
element.click()
sleep(3)
alert=driver.switch_to.alert
alert.dismiss()# it will select the cancel
sleep(5)
driver.quit()
