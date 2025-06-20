from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Lancer le navigateur
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com")
time.sleep(2)  # Laisse le temps au site de charger

# Remplir les champs
driver.find_element(By.ID, "name").send_keys("Yohan")
driver.find_element(By.ID, "email").send_keys("yohan@test.com")
driver.find_element(By.ID, "phone").send_keys("0601020304")
driver.find_element(By.ID, "textarea").send_keys("123 rue de Python")

# Choisir le genre : Male
driver.find_element(By.ID, "male").click()

# Cocher une checkbox (ex: Sunday)
driver.find_element(By.ID, "sunday").click()

# Sélectionner un pays dans Country
Select(driver.find_element(By.ID, "country")).select_by_visible_text("France")

# Cliquer sur le bouton Submit (il faut scroller parfois)
driver.find_element(By.ID, "submit").click()

# Vérification console
print("✅ Formulaire soumis avec succès.")
time.sleep(5)
driver.quit()
