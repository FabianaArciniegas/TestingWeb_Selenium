import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

# Configuracion del navegador
chrome_options = Options()
service = Service("Driver/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.maximize_window()

# Navegar a la pagina
driver.get("http://localhost:63342/ConceptosTestingSelenium/html-ejm/confirm.html?_ijt=e0ks9u4ekobc0jk5fbt841bnr1")
time.sleep(3)

# Acceder al boton
boton = driver.find_element(By.NAME, "boton")
boton.click()
time.sleep(3)

# Acceder al confirm
driver.switch_to.alert.accept()
time.sleep(3)

# Salir
driver.quit()
