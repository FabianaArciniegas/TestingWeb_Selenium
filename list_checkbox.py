import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Configuracion del navegador
chrome_options = Options()
service = Service("Driver/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.maximize_window()

# Navegar a la pagina
driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
time.sleep(5)

# Acceder a todos los checkbox
checkbox = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')

for check in checkbox:
    if check.is_displayed() is True and check.is_selected() is False:
        check.click()
        time.sleep(3)

# Acceder a todos los checkmark (QUEDA PENDIENTE POR REVISAR - NO ME SALE ERROR PERO NO ME FUNCIONA)
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//span[@class="checkmark"]')))
checkmarks = driver.find_elements(By.XPATH, '//span[@class="checkmark"]')

for checkmark in checkmarks:
    # Encontrar el elemento `input` relacionado
    parent_label = checkmark.find_element(By.XPATH, '..')  # El padre `<label>`
    time.sleep(3)
    related_input = parent_label.find_element(By.XPATH, './input[@type="checkbox"]')
    time.sleep(3)

    if related_input.is_displayed():
        if not related_input.is_selected():
            driver.execute_script("arguments[0].click();", parent_label)
            time.sleep(3)
            print("Checkbox personalizado seleccionado.")
        else:
            print("Checkbox personalizado ya estaba seleccionado. No se realiza ninguna acción.")
        time.sleep(3)

# Salir
driver.quit()
