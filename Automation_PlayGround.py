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

#Login Usecase
driver.find_element(By.ID, "email-id").send_keys("123aqw@gmail.com")
driver.find_element(By.ID, "password").send_keys("rightfit")
driver.find_element(By.ID, "remember").click()
driver.find_element(By.ID, "submit-id").click()
time.sleep(3)

#New Customer
driver.find_element()

#Fill new customer form
driver.find_element()

#Sign Out
driver.find_element()
#Quit browser
driver.quit()

