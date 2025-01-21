from src import math_operations, string_operations
import unittest

class TestSafetyOpeations(unittest.TestCase):
    def test_additionner(self):
        self.assertEqual(math_operations.additionner(1,3),4)

    def test_soustraire(self):
        self.assertEqual(math_operations.soustraire(4,3),1)
    
    def test_multiplier(self):
        self.assertEqual(math_operations.multiplier(2,3),6)

    def test_diviser(self):
        self.assertEqual(math_operations.diviser(4,2),2)


if __name__ == "__main__":
    unittest.main()
    
    