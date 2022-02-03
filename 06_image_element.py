from selenium import webdriver
from time import sleep

#image attribute
# driver = webdriver.Chrome()
# driver.get("https://www.wikipedia.org/")
# element=driver.find_element_by_class_name("central-featured-logo")
# print (element.tag_name)
# print (element.size)
# print (element.location)
# print ("Image displayed ", element.is_displayed())
# print("src :",element.get_attribute('src'))
# print("height :",element.get_attribute('height'))
# print("width :",element.get_attribute('width'))
# print("alt :",element.get_attribute('alt'))
# print("srcset :",element.get_attribute('srcset'))
# d=element.size
# if (d['height']==183):
#     print("Height is expected and test pass")
# else:
#     print("Height is not as expected and test fail")
# sleep(2)
# driver.quit()
# =========================
# Broken images

from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
URL = "https://the-internet.herokuapp.com/broken_images"
iBrokenImageCount = 0

driver.get(URL)
image_list = driver.find_elements(By.TAG_NAME, "img")
print('Total number of images on ' + URL + ' are ' + str(len(image_list)))

for img in image_list:
    try:
        response = requests.get(img.get_attribute('src'), stream=True)
        if (response.status_code != 200):
            print(img.get_attribute('outerHTML') + " is broken.")
            iBrokenImageCount = (iBrokenImageCount + 1)

    except requests.exceptions.MissingSchema:
        print("Encountered MissingSchema Exception")
    except requests.exceptions.InvalidSchema:
        print("Encountered InvalidSchema Exception")
    except:
        print("Encountered Some other Exception")

driver.quit()

print('The page ' + URL + ' has ' + str(iBrokenImageCount) + ' broken images')