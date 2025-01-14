import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Configuracion inicial del navegador
chrome_options = Options()
service = Service("Driver/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.maximize_window()

# Navegar a la página
driver.get("https://p4s.co/login")
time.sleep(5)

# Autenticación login
user_email = driver.find_element(By.ID, "email")
user_email.send_keys("xxxx@example.com")

user_password = driver.find_element(By.ID, "passwd")
user_password.send_keys("12345")

login_button = driver.find_element(By.CSS_SELECTOR, "input[value='Ingresar']")
login_button.click()
time.sleep(5)

# Salir
driver.close()
