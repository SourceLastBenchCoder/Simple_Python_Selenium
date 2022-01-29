from selenium import webdriver

import time

from selenium.webdriver.common.keys import Keys

print("Started")

driver = webdriver.Chrome("E:\Drivers\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.google.com/")

driver.find_element_by_name("q").send_keys("Python Learning")

time.sleep(3)

driver.find_element_by_name("btnK").send_keys(Keys.ENTER)

time.sleep(3)

print("Ended")

driver.close()