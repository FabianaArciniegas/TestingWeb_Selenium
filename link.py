import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Configuración del navegador
chrome_options = Options()
service = Service("Driver/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.maximize_window()

# Navegar a la página
driver.get("https://p4s.co/login")
time.sleep(5)

# Recuperacion de contraseña
link_recuperation = driver.find_element("link text", "Recuperar Password")
link_recuperation.click()
time.sleep(5)

# Ingresar email
email_input = driver.find_element("xpath", '//*[@id="email"]')
email_input.send_keys("xxxx@example.com")
time.sleep(5)

# Enviar email
send_button = driver.find_element("xpath", '//*[@value="Enviar"]')
send_button.click()
time.sleep(5)

# Salir
driver.quit()
