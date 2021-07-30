from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://en.wikipedia.org")
sleep(3)
driver.execute_script("document.body.style.zoom='250%'")
s=driver.execute_script("return document.title")
print(s)
print (driver.execute_script("return document.title"))
print(driver.execute_script("return document.URL"))
print(driver.execute_script("return document.Domain"))
sleep(2)
driver.execute_script("window.scrollBy(0,800)")
driver.execute_script("document.body.style.zoom='100%'")

sleep(5)
driver.quit()