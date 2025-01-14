import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Configuracion del navegador
chrome_options = Options()
service = Service("Driver/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.maximize_window()

# Navegar a la pagina inicial
driver.get("https://p4s.co/news/")
time.sleep(5)

# Abrir nueva pestaña y navegar
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://p4s.co/login")
time.sleep(3)

# Abrir otra nueva pestaña y navegar
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
driver.get("https://p4s.co/tutoriales")
time.sleep(3)

# Cerrar la pestaña
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
driver.close()

# Cerrar la pestaña
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
driver.close()

# Cerrar el navegador
time.sleep(3)
driver.quit()
