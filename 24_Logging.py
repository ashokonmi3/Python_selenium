from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import logging

LOG_FILENAME='logging_warning121.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
# CRITICAL', 'DEBUG', 'ERROR', 'FATAL',  'INFO',
# driver = webdriver.Ie()
driver = webdriver.Chrome()

logging.debug("Browser started")
driver.maximize_window()
driver.get("http://www.pyasdfthon.org")


logging.debug("maximized")
print driver.capabilities['version']
logging.debug("version printed")

sleep(3)
driver.quit()

# print dir(logging)
