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


# Autenticación login
# (este es ruta absoluta - puede estar afectada solo si se cambia la estructura de la página)
user_email = driver.find_element("xpath", '/html[1]/body[1]/div[6]/div[1]/div[1]/div[1]/div[1]/form[1]/input[1]')
user_email.send_keys("xxxx@example.com")

# (este es ruta relativa - es mas recomendada)
user_password = driver.find_element("xpath", '//input[@id="passwd" and @type="password"]')
user_password.send_keys("12345")

# (este es ruta relativa - es mas recomendada)
login_button = driver.find_element("xpath", '//input[@value="Ingresar" and @type="submit"]')
login_button.click()
time.sleep(5)
