from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
path = os.getcwd()
print(path)

driver = webdriver.Chrome(path+"/chromedriver")
driver.get("http://www.python.org")