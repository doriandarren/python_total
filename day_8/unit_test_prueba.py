import unittest
import unit_test_texto

class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = 'buen dia'
        resultado = unit_test_texto.todo_mayuscula(palabra)
        self.assertEqual(resultado, 'BUEN DIA')


if __name__ == '__main__':
    unittest.main()