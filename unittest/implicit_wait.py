import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class implicit_wait_unittest(unittest.TestCase):

    # Es una precondicion, siempre se va a ejecutar en cada test case
    def setUp(self):
        # Configuracion del navegador
        self.chrome_options = Options()
        self.service = Service("../Driver/chromedriver.exe")
        self.driver = webdriver.Chrome(options=self.chrome_options, service=self.service)
        self.driver.maximize_window()

    def test_implicit_wait(self):
        # Navegar a la pagina
        self.driver.get("https://p4s.co/login")

        # Esperar a que se cargue el elemento
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
