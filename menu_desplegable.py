import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select

# Configuracion del navegador
chrome_options = Options()
service = Service("Driver/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.maximize_window()

# Navegar a la pagina
driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
time.sleep(5)

# Acceder al select
select = driver.find_element(By.XPATH, '/html[1]/body[1]/div[5]/div[1]/div[1]/div[3]/div[1]/select[1]')

# Acceder a todas las opciones usando Select
options = Select(select).options

# Acceder a todas las opciones
# options = driver.find_elements(By.TAG_NAME, 'option')

for option in options:
    # Desplazarse hasta la opción
    driver.execute_script("arguments[0].scrollIntoView(true);", option)

    # Esperar a que la opción sea visible y clickable
    WebDriverWait(driver, 10).until(EC.visibility_of(option))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(option))

    # Hacer clic en la opción
    option.click()
    time.sleep(3)

# Salir
driver.quit()
