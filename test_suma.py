import unittest 
from suma import sumar
import unittest 
from suma import restar
import unittest 
from suma import multiplicar
import unittest 
from suma import dividir

class TestSumar(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3,2,), 5)
        self.assertEqual(sumar(-1,1,), 0)
        self.assertEqual(sumar(-1,-1,), -2)
        self.assertEqual(restar(3,2,), 1)
        self.assertEqual(restar(-1,1,), -2)
        self.assertEqual(restar(-1,-1,), 0)
        self.assertEqual(multiplicar(2,5,), 10)
        self.assertEqual(multiplicar(2,-5,), -10)
        self.assertEqual(multiplicar(0,0,), 0)
        self.assertEqual(dividir(4,2,), 2)
        self.assertEqual(dividir(0,0,), 0)
        self.assertEqual(dividir(-5,-5,), 1)

if __name__ == '__main__':
    unittest.main()