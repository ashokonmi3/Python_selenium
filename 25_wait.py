from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
# driver = webdriver.Ie()
# driver.implicitly_wait(30)

#chromedriver = 'chromedriver.exe'
# driver = webdriver.Chrome()
# driver.implicitly_wait(30)
# driver.get("http://www.python.org")
# elem = driver.find_element_by_name("q")
# driver.get("http://www.DemoQA.com")
# # driver.navigate().to("http://www.DemoQA.com")
# driver.get("http://www.python.org")
# elem = driver.find_element_by_name("q1")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID,'submit')))
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("biycon")
# elem.send_keys(Keys.RETURN)
# assert "No Result found." not in driver.page_source
driver.close()


#  title_is
#  title_contains
#  presence_of_element_located
#  visibility_of_element_located
#  visibility_of
#  presence_of_all_elements_located
#  text_to_be_present_in_element
#  text_to_be_present_in_element_value
#  frame_to_be_available_and_switch_to_it
#  invisibility_of_element_located
#  element_to_be_clickable - it is Displayed and Enabled.
#  staleness_of
#  element_to_be_selected
#  element_located_to_be_selected
#  element_selection_state_to_be
#  element_located_selection_state_to_be
#  alert_is_present

# from selenium.webdriver import ActionChains 
# element = driver.find_element_by_name("source") 
# target = driver.find_element_by_name("target") 
# action_chains = ActionChains(driver) 
# action_chains.drag_and_drop(element, target).perform()


# if(driver.findElement(By.xpath(noRecordId)).isDisplayed() )                                                                                                         
# {         
#   /**Do this*/     
# }    
# else    
# {     
#   /**Do this*/    
# }


# isSelected():
# boolean buttonSelected = driver.findElement(By.id("python")).isDisplayed();

# isEnabled():
# boolean searchIconEnabled = driver.findElement(By.id(python)).isEnabled();


# Getting the text of and element
# String Text = driver.findElement(By.id(Text)).getText();



# ======================================================
# Drop down menu
# -----------------
# <select id="package" class="select" name="course">
#     <option value="0">Choose your fruits:</option>
#     <option value="1">python</option>
#     <option value="2">java</option>
# </select>
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select

# driver = webdriver.Firefox()
# driver.get('url')

# select = Select(driver.find_element_by_id('package'))

# # select by visible text
# select.select_by_visible_text('Banana')

# # select by value 
# select.select_by_value('1')
# # select by index

# select.select_by_index('1')
# ================
# driver.switchTo().alert().dismiss();
# driver.switchTo().alert().accept();
# driver.switchTo().alert().getText();	
# driver.switchTo().alert().sendKeys("Text");


# ===========================
# screen shot 
# driver.save_screenshot('/path/to/file') or 
# driver.get_screenshot_as_file('/path/to/file'):
# ===============================
# Compare images
# import cv2
