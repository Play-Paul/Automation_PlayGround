from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(3)
driver.maximize_window()
driver.get("https://google.com")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ntp-app//div/div[2]/cr-searchbox//div/input").click()
driver.find_element(By.XPATH, "/html/body/ntp-app//div/div[2]/cr-searchbox//div/input").send_keys("rain guage types")

time.sleep(3)
driver.quit()