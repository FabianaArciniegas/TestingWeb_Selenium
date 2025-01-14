import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.service import Service

# Configuracion del navegador
chrome_options = Options()
service = Service("Driver/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.maximize_window()

# Navegar a la pagina
driver.get("https://www.google.com/")
time.sleep(5)

# Abrir nueva pestaña y navegar
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.google.com/")
time.sleep(3)
driver.get("https://www.facebook.com/")
time.sleep(3)

# Abrir nueva pestaña y navegar
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
driver.get("https://www.google.com/")
time.sleep(3)
driver.get("https://www.youtube.com/")
time.sleep(3)

# Ir hacia atras en la misma pestaña
driver.back()
time.sleep(3)

# Regresar a la segunda pestaña
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)

# Ir hacia atras en la misma pestaña
driver.back()
time.sleep(3)

# Regresar y cerrar la primera pestaña
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
driver.close()
time.sleep(3)

# Regresar y cerrar la segunda pestaña
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
driver.close()
time.sleep(3)

# Ir hacia adelante en la misma pestaña
driver.switch_to.window(driver.window_handles[0])
driver.forward()
time.sleep(3)

# Cerrar todas las pestañas
driver.quit()
