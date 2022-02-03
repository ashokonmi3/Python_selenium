from selenium import webdriver
from time import sleep

#Partial link text attribute
# driver = webdriver.Chrome()
# driver.get("https://ashokonmi3.github.io/Selenium.Pages/FindElements.html")
# driver.find_element_by_partial_link_text("Webdriver").click()
# driver.quit()

# =========================
driver = webdriver.Chrome()
driver.get("https://ashokonmi3.github.io/Selenium.Pages/FindElements.html")
driver.find_element_by_link_text("Selenium Webdriver").click()
driver.quit()
