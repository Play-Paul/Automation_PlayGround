from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(3)
driver.maximize_window()
driver.get("https://www.jumia.com.ng/")
time.sleep(5)
driver.quit()