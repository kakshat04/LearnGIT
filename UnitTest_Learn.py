import unittest
from Calculate_Test import *
from math import pi


class TestCal(unittest.TestCase):
    def setUp(self):
        self.x = TestCalculate(10, 5)

    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual(self.x.addition, 15)

    def test_sub(self):
        # x = TestCalculate(5,2)
        self.assertEqual(self.x.subtract(), 5)

    def test_mul(self):
        # x = TestCalculate(5,2)
        self.assertEqual(self.x.multiply(), 50)

    def test_div(self):
        # x = TestCalculate(6,2)
        self.assertEqual(self.x.divide(2), 5)
        self.assertRaises(ValueError, self.x.divide, 0)

    def test_mod(self):
        self.assertEqual(modulus(10,2), 0)
        with self.assertRaises(ValueError):
            modulus(10, 0)

    def test_area(self):
        area = TestArea(2)
        self.assertAlmostEqual(area.circle(), pi * 2**2)

    def test_valueError(self):
        area = TestArea(0)
        self.assertRaises(ValueError, area.circle)


if __name__ == '__main__':
    unittest.main()