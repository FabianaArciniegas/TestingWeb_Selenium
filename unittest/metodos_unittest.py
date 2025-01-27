import unittest


class unittest_methods(unittest.TestCase):

    # Se ejecuta una sola vez
    @classmethod
    def setUpClass(cls):
        print("Yo me ejecuto al inicio de la clase")

    # Es un metodo que me permite predefinir ciertas condiciones que se deben de tomar antes de iniciar cada test case
    def setUp(self):
        print("Yo me inicio en cada test case")

    # Es un metodo propio - por ello la palabra "test"  (en los metodos reservados no se usa "test")
    def test_message(self):
        print("Yo soy el test case del mensaje")

    # Es un metodo propio - por ello la palabra "test"
    def test_number(self):
        print("Yo soy el test case del numero")

    # Es un metodo que se ejecuta al final de cada test case
    def tearDown(self):
        print("Yo me cierro en cada test case")

    # Se ejecuta una sola vez
    @classmethod
    def tearDownClass(cls):
        print("Yo me ejecuto al final de la clase")


if __name__ == '__main__':
    unittest.main()
