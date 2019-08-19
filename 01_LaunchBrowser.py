from selenium import webdriver
from time import sleep
browser=webdriver.Chrome()
print (dir(browser))
browser.get('https://www.python.org')
sleep(15)
browser.close()
# pip install sellenium
