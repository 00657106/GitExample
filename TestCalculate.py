import unittest
import calculate
class TestCalculate(unittest.TestCase):
    def test_int_add(self):
        self.assertEqual(calculate.add(8, 9), 17)
    def test_float_add(self):
        self.assertEqual(calculate.add(8.7, 9.1), 17.8)
    def test_int_decrease(self):
        self.assertEqual(calculate.decrease(9, 3), 6)
    def test_float_decrease(self):
        self.assertEqual(calculate.decrease(9, 4.8), 4.2)
    def test_int_multiply(self):
        self.assertEqual(calculate.multiply(8, 7), 56)
    def test_float_multiply(self):
        self.assertEqual(calculate.multiply(8.2, 3.6), 29.52)
    def test_int_divided(self):
        self.assertEqual(calculate.divide(6, 2), 3)
    def test_float_divided(self):
        self.assertEqual(calculate.divide(4.2, 2.1), 2.0)
    def test_infinite_divided(self):
        self.assertEqual(calculate.divide(4, 0), "infinite")
if __name__ == '__main__':
    unittest.main()