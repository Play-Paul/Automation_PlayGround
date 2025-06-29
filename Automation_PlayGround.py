from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Initialise webdriver
driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()

#Call url
driver.get("https://automationplayground.com/crm/login.html")
time.sleep(3)

#Quit browser
driver.quit()

