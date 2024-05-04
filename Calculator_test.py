import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        result = self.calc.add(3, 5)
        self.assertEqual(result, 8)

    def test_subtract(self):
        result = self.calc.subtract(10, 3)
        self.assertEqual(result, 7)

    def test_multiply(self):
        result = self.calc.multiply(2, 4)
        self.assertEqual(result, 8)

    def test_divide(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
