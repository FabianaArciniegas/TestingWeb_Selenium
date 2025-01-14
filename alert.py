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
driver.get("http://localhost:63342/ConceptosTestingSelenium/html-ejm/alert.html?_ijt=3ifq5i9l0hlehv2tqakgsb757p")
time.sleep(3)

# Acceder al boton
boton = driver.find_element(By.ID, "btn")
boton.click()
time.sleep(3)

# Acceder al alert
driver.switch_to.alert.dismiss()
time.sleep(3)

# Salir
driver.quit()
