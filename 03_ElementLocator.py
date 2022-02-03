from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# Element Locator- 8 type of element locator
# 1 Classname
# 2 Id
# 3 Name
# 4 tag
# 5 linktext
# 6 Xpath
# 7 CSS
# 8 partiallinktext

# find_element_by_id()
# • find_element_by_name()
# • find_element_by_xpath()
# • find_element_by_css_selector()
# • find_element_by_link_text()
# • find_element_by_partial_link_text()
# • find_element_by_class_name()
# • find_element_by_tag_name()

# Apart	from	the	methods	given	above,	there is	one	more method
# which	might	be	useful	->	find_element().
# driver.find_element(By.XPATH,		"xpath	expression")
# These	are	the	attributes	available	for	By:
# • ID	=	"id"
# • NAME	=	"name"
# • XPATH	=	"xpath	expression"
# • CSS_SELECTOR	=	"css	selector	expression"
# • LINK_TEXT	=	"link	text"
# • PARTIAL_LINK_TEXT	=	"partial	link	text"
# • CLASS_NAME	=	"class	name"
# • TAG_NAME	=	"tag	name"
# #
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://www.calculator.net/bmi-calculator.html")
# age_box=driver.find_element_by_name("cage")
# sleep(5)
# age_box.clear()
# age_box.send_keys("45")
# height_box=driver.find_element_by_id("cheightmeter")
# height_box.clear()
# height_box.send_keys("5")
# weight_box=driver.find_element_by_name("ckg")
# weight_box.clear()
# weight_box.send_keys("50")
# sleep(2)
# # click_button=driver.find_element_by_xpath("//input[@type='image']")
# # click_button.click()
# sleep(5)
# driver.quit()
# ====================================
# driver = webdriver.Chrome()
# driver.get("http://www.google.com")
# sleep(2)
# link_element=driver.find_element_by_link_text("Gmail")
# link_element.click()
# sleep(2)
# driver.quit()
# =========================
# driver = webdriver.Chrome()
# driver.get("http://www.rediff.com")
# sleep(2)
# element=driver.find_element_by_class_name("homesrchbox")
# element.send_keys("Reliance")
# element.send_keys(Keys.RETURN)
# sleep(2)
# driver.quit()
# =====================
# driver = webdriver.Chrome()
# driver.get("https://ashokonmi3.github.io/Selenium.Pages/css_xpath.html")
# sleep(2)
# element=driver.find_element_by_css_selector("#pancakes > a")
# element.click()
# sleep(2)
# driver.quit()
# ==============
# driver = webdriver.Chrome()
# driver.get("https://ashokonmi3.github.io/Selenium.Pages/css_xpath.html")
# sleep(2)
# element=driver.find_element_by_xpath("//*[@id='pancakes']/a")
# element.click()
# sleep(2)
# driver.quit()
# ===========================
# driver = webdriver.Chrome()
# driver.get("https://ashokonmi3.github.io/Selenium.Pages/FindElements.html")
# sleep(2)
# elements=driver.find_elements_by_id("firstButton")
# print(elements)
# print(f" total no of first button elements are {len(elements)}")
# driver.quit()
# =================
driver = webdriver.Chrome()
driver.get("http://www.rediff.com")
sleep(2)
elements=driver.find_elements_by_tag_name("img")
print(elements)
print(f" total no of images are {len(elements)}")
driver.quit()
