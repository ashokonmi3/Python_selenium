# sendKeys()
# clear()
# isenabled()
# isdisplayed()
# Getattribute()
# ======================
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# driver = webdriver.Chrome()
# driver.get("https://ashokonmi3.github.io/Selenium.Pages/login.html")
# sleep(2)
#
# elem = driver.find_element_by_name("username")
# elem.clear()
# elem.send_keys("root")
# driver.find_element_by_name("password").send_keys("root")
# driver.find_element_by_xpath("/html/body/form/input[3]").send_keys(Keys.ENTER)
# sleep(5)
# driver.close()
# ========================
# driver = webdriver.Chrome()
# driver.get("https://google.com")
# sleep(2)
# a = "java "
# driver.find_element_by_name("q").send_keys(a, "Selenium -", "varargs")
# sleep(5)
# driver.close()
# ===============================
# Get attribute
# driver = webdriver.Chrome()
# driver.get("https://ashokonmi3.github.io/Selenium.Pages/login.html")
# sleep(2)
#
# elem = driver.find_element_by_name("username")
# elem.clear()
# elem.send_keys("root")
# print(elem.get_attribute("type"))
# print(elem.get_attribute("value"))
# sleep(5)
# driver.close()
# ============================
driver = webdriver.Chrome()
driver.get("https://ashokonmi3.github.io/Selenium.Pages/disabledEditBox.html")
sleep(2)

elem = driver.find_element_by_name("lname")
sleep(5)
print(elem.is_enabled())
print(elem.is_displayed())
driver.close()
