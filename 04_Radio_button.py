from selenium import webdriver
from time import sleep

# Radio button
# Check box
# Operation allowed
# select
# deselect
# isselected --
# isDisplayed
# isEnabled
# ===========================
# driver = webdriver.Chrome()
# driver.get("https://ashokonmi3.github.io/Selenium.Pages/SEL_01_WebDriverDemoWebsite.html")
# radio_button = driver.find_element_by_id("magazines-radio-btn")
# radio_button.click()
# checkbox = driver.find_element_by_id("bicycle-checkbox")
# sleep(2)
# print("Before clicking " , checkbox.is_selected())
# checkbox.click()
# sleep(2)
# print("After clicking " , checkbox.is_selected())
# print("After is_displayed " , checkbox.is_displayed())
#
# driver.close()
# =======================
# is_enabled()
driver = webdriver.Chrome()
driver.get("https://ashokonmi3.github.io/Selenium.Pages/Web_Elements.html")
radio_button = driver.find_element_by_id("tricycle-checkbox")
print(f"Tricycle check box enable status  {radio_button.is_enabled()}")
driver.close()



