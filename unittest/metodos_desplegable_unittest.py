import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.ui import Select


class dropdown_menu_unittest(unittest.TestCase):

    # Es una precondicion, siempre se va a ejecutar en cada test case
    def setUp(self):
        # Configuracion del navegador
        self.chrome_options = Options()
        self.service = Service("../Driver/chromedriver.exe")
        self.driver = webdriver.Chrome(options=self.chrome_options, service=self.service)
        self.driver.maximize_window()

    def test_recorrer_opciones(self):
        # Navegar a la pagina
        self.driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        time.sleep(5)

        # Acceder al select
        menu = Select(
            self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[5]/div[1]/div[1]/div[3]/div[1]/select[1]'))
        time.sleep(3)

        # Escoger una opcion especifica, mediante index
        menu.select_by_index(11)
        time.sleep(3)

        # Escoger una opcion especifica, mediante value
        menu.select_by_value("6")
        time.sleep(3)

        # Escoger una opcion especifica, mediante visible text (No es recomendable, por cambios futuros en el texto)
        menu.select_by_visible_text("Ford")
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
