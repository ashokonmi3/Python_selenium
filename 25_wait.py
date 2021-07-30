from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# elem = driver.find_element_by_name("q1")
# driver.close()
# ======================
# driver = webdriver.Chrome()
# driver.implicitly_wait(30)
# driver.get("http://www.python.org")
# elem = driver.find_element_by_name("q1")
# driver.close()

# ============================
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("http://www.python.org")
element = wait.until(EC.element_to_be_clickable((By.ID,'submit')))
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("biycon")
elem.send_keys(Keys.RETURN)
assert "No Result found." not in driver.page_source
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


# if(driver.findElement(By.xpath(noRecordId)).isDisplayed() )                                                                                                         
# {         
#   /**Do this*/     
# }    
# else    
# {     
#   /**Do this*/    
# }


