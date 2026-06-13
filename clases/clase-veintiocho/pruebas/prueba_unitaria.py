import unittest
from funciones_a_probar import sumar

class TestSumar(unittest.TestCase):
    def test_sumar_positivos(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_sumar_negativos(self):
        self.assertEqual(sumar(-2, -3), -5)

    def test_sumar_mixtos(self):
        self.assertEqual(sumar(-2, 3), 1)

if __name__ == '__main__':
    unittest.main()