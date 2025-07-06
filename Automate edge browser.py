from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
driver.get("https://web.facebook.com/")
time.sleep(3)
driver.find_element(By.ID, "email").send_keys("info.playpro@gmail.com")
driver.find_element(By.ID, "pass").send_keys("thebatcave")
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/button[1]").click()
time.sleep(3)