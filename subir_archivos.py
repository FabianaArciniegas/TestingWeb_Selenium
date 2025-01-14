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
driver.get("https://www.w3schools.com/howto/howto_html_file_upload_button.asp")
time.sleep(5)

# Subir archivo
boton = driver.find_element(By.ID, "myFile")
boton.send_keys(r"D:\Users\Dennys\Downloads\diagrama-clases-gein.drawio.png")
time.sleep(5)

# Salir
driver.quit()
