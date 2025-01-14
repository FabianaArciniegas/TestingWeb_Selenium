import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class explicit_wait_unittest(unittest.TestCase):

    def setUp(self):
        # Configuracion del navegador
        self.chrome_options = Options()
        self.service = Service("../Driver/chromedriver.exe")
        self.driver = webdriver.Chrome(options=self.chrome_options, service=self.service)
        self.driver.maximize_window()

    def test_explicit_wait(self):
        # Navegar a la pagina
        self.driver.get("https://p4s.co/login")

        # Esperar a que se cargue el elemento
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
