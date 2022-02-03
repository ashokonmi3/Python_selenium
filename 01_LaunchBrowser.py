# 1. Download the sublime text editor(pycharm) and install
# 2. Download the chromedriver.exe( Chrome)
# 3. Add the location of chromedriver into the path variable
# 4. Check python is installed in your machine by typing the  python --version in command version
# 5. Install the python (3.6/7) if not installed
# 6. Install the selenium using command 'pip install selenium'
# Create virtual environment selenv "python -m  venv selenv"
# selenv\Scripts\activate.bat to activate the environment
# python --version
# pip install selenium

from selenium import webdriver
from time import sleep
# browser=webdriver.Chrome()
# driver = webdriver.Chrome(executable_path=r'path/to/folder/chromedriver.exe')

# firfox_browser= webdriver.Firefox()
# ie_browser= webdriver.Ie()
print (dir(browser))
browser.get('https://www.python.org')
# browser.get('https://www.rediff.com')
sleep(5)
browser.close()
