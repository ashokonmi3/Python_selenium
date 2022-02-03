from selenium import webdriver
from time import sleep
import logging
#
# LOG_FILENAME= 'logging_warning1702.log'
# logging.basicConfig(filename=LOG_FILENAME,level=logging.WARN)
# # DEBUG', 'INFO', 'WARNING', 'ERROR',  'CRITICAL',
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')
# ==================
LOG_FILENAME= 'logging_warning170211.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
driver = webdriver.Chrome()
logging.debug("Browser started")
driver.get("http://www.python1.org")
if (driver.current_url !="http://www.python.org"):
    logging.error("webpage http://www.python.org is not launched")
logging.debug("maximized")
print(driver.capabilities)
print (driver.capabilities['browserVersion'])
logging.debug("browserVersion printed")
sleep(3)
# print(s)
driver.quit()
# print(__file__)
# import os
# print dir(logging)
# print(os.path.dirname(__file__))

