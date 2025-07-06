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
driver.find_element(By.ID, "new-customer").click()
driver.find_element(By.ID, "EmailAddress").send_keys("info.playprostudios@gmail.com")
driver.find_element(By.ID, "FirstName").send_keys("Emeka")
driver.find_element(By.ID, "LastName").send_keys("Paul")
driver.find_element(By.ID, "City").send_keys("Eko Ni Show")
driver.find_element(By.ID, "StateOrRegion").send_keys("Maryland")
driver.find_element(By.XPATH, "//input[@value='male']").click()
driver.find_element(By.XPATH, "//input[@name='promos-name']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
driver.find_element(By.CSS_SELECTOR, ".nav-link")
time.sleep(5)
driver.quit()

