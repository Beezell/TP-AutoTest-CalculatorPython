from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.set_window_size(1298, 952)
driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, ".fa").click()

time.sleep(5)  # Pause assez longue pour que tu voies le résultat

message = driver.find_element(By.ID, "flash").text
print("Message affiché :", message)

time.sleep(5)  # Garde la fenêtre visible un peu plus
driver.quit()
