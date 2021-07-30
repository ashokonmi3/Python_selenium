from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
print("In parent window ")
print("switching to frame 2 by method switch_to_frame(2) ")
driver.switch_to.frame(2)
sleep(3)
driver.find_element_by_link_text("org.openqa.selenium").click()
sleep(3)
print("In frame 2 now ")
print("To go to frame 0 first need to go to parent window")
print("Going to parent window by function switch_to_default_content()")
driver.switch_to.default_content()
sleep(3)
print("In parent window now")
print("switching to frame 0 by function driver.switch_to_frame(0)")
driver.switch_to.frame(0)
driver.find_element_by_link_text("org.openqa.selenium").click()
sleep(3)
driver.switch_to.default_content()

driver.quit()

