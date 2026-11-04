import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add1(self):
        self.assertEqual(self.calc.add(6, 7), 13)
    def test_add2(self):
        self.assertEqual(self.calc.add(2, 2), 4)

    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(4, 4), 0)
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(-1, 2), -2)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(-6, -6), 36)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
    def test_divide(self):
        self.assertEqual(self.calc.divide(0, 1), 0)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(2, -1), 2)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(3, 0), 3)

if __name__ == '__main__':
    unittest.main()
