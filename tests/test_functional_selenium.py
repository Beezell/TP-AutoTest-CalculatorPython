import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_addition():
    # Choix du chromedriver selon l'OS
    if sys.platform.startswith("win"):
        service = Service("drivers/chromedriver.exe")
    else:
        service = Service("drivers/chromedriver")  # version Linux, sans .exe

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # mode sans interface graphique
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("http://localhost:5000")

    # Remplir les champs
    driver.find_element(By.NAME, "a").send_keys("3")
    driver.find_element(By.NAME, "b").send_keys("4")
    driver.find_element(By.NAME, "operation").send_keys("addition")

    # Soumettre le formulaire
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(1)  # attendre le chargement

    # Vérifier que le résultat s'affiche bien
    assert "Résultat : 7" in driver.page_source

    driver.quit()
