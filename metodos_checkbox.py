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
driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
time.sleep(5)

# Acceder al checkbox
checkbox = driver.find_element(By.XPATH, '/html[1]/body[1]/div[5]/div[1]/div[1]/div[3]/div[1]/input[1]')

print(checkbox.is_selected())  # Si esta seleccionado
print(checkbox.is_enabled())  # Si esta habilitado
print(checkbox.is_displayed())  # Si esta visible

# Salir
driver.quit()
