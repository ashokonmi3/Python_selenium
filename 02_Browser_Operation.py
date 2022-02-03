# Operations on a web browser:
# 1) Launch a url
# 2) Maximize the window
# 3) Read current url
# 4) back forward
# 5) close the browser
# 6) Refresh the browser
# 7) Resize of browser
# 8) Read the page source of a web page
# 9) Getting the browser capabilities

# Browser 'Interaction'And'Navigating'Web'Pages
# Some attributes are methods and others are properties.
# All the method attributes are ending with round brackets.
# Command Description Method/Property
# maximize_window() Maximizes the current window that webdriver is using  Method
# driver.get(url) Loads a web page in the current  browser session. Method
# driver.title Returns the title of the current page. Property
# driver.current_url URL of the current loaded page. Property
# driver.refresh() Refreshes the current page. Method
# driver.get(driver.current_url) Refreshes the current page. Method
# driver.back() Goes one step backward in the browser history. Method
# driver.forward() Goes one step forward in the browser history. Method
# driver.page_source Gets the source of the current page. Property
# driver.close() Closes the current window Method
# driver.quit() Quits the driver and close every associated window. Method

from selenium import webdriver
from time import sleep
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.zkoss.org/zkdemo/input/radio_button")
# current_url=driver.current_url
# print (driver.current_url)
# if (current_url=="https://www.zkoss.org/zkdemo/input/radio_button"):
# 	print("Test case pass")
# else:
# 	print("test failed")
# sleep(5)
# driver.quit()
# # ===================================
# # Soure code of page
# driver = webdriver.Chrome()
# driver.get("http://google.com")
# doc= driver.page_source
# print (doc)
# if "Copyright (c) 2010 Robert Kieffer" in doc:
# 	print( "test pass")
# else:
# 	print ("test failed")
# driver.quit()
# # ==========================
# # Navigation
# def validate_currenturl(driver,url):
#     print(driver.current_url)
#     if (driver.current_url == url):
#         print("Test case pass")
#     else:
#         print(f"test failed current url is not {url}")
#
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# validate_currenturl(driver,"https://www.python.org/")
#
# elem = driver.find_element_by_link_text("Community")
# sleep(5)
# elem.click()
# sleep(5)
# validate_currenturl(driver,"https://www.python.org/community-landing/")
# driver.back()
# validate_currenturl(driver,"https://www.python.org/")
#
# sleep(5)
# driver.forward()
# validate_currenturl(driver,"https://www.python.org/community-landing/")
# sleep(5)
#
# driver.quit()
# ===============
# Window size
# driver = webdriver.Chrome()
# driver.maximize_window()
# print(driver.get_window_size())
# driver.get("https://google.com")
# print("changing the size)")
# driver.set_window_size(1024,768)
# sleep(3)
# print(driver.get_window_size())
# driver.maximize_window()
# sleep(5)
# print(driver.get_window_size())
# sleep(5)
# driver.close()
# ======================
# Window position and refresh
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://google.com")
# sleep(3)
# driver.refresh()
# sleep(3)
# driver.set_window_position(150,200)
# sleep(3)
# print(driver.get_window_position())
# driver.set_window_position(350,400)
# sleep(3)
# driver.close()
# ======================
# Browser version
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://google.com")
print (driver.capabilities)# dictionary
print (driver.capabilities['browserVersion'])
sleep(5)
driver.quit()