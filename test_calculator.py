import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()


    # Add method
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_negativeadd(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    # Subtract method
    def test_positivesub(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)

    def test_negativesub(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)

    def test_zerosub(self):
        self.assertEqual(self.calc.subtract(1, 1), 0)


    # Multiply method
    def test_positivemul(self):
        self.assertEqual(self.calc.multiply(1, 2), 2)

    def test_positive2mul(self):
        self.assertEqual(self.calc.multiply(-1, -2), 2)

    def test_negativemul(self):
        self.assertEqual(self.calc.multiply(1, -2), -2)

    def test_zeromul(self):
        self.assertEqual(self.calc.multiply(0, 0), 0)    

    # Div method
    def test_positivediv(self):
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_positive2div(self):
        self.assertEqual(self.calc.divide(-10, -5), 2)

    def test_negativediv(self):
        self.assertEqual(self.calc.divide(10, -5), -2)

    def test_negative2div(self):
        self.assertEqual(self.calc.divide(-10, 5), -2)        

    def test_zerodiv(self):
        self.assertEqual(self.calc.divide(0, 0), 'Undefined')


    # Modulo method
    def test_positivemod(self):
        self.assertEqual(self.calc.modulo(10, 5), 0)

    def test_positive2mod(self):
        self.assertEqual(self.calc.modulo(10, 7), 3)
    
    
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()