import unittest
import conversion

class TestSafetyConversion(unittest.TestCase):
    def test_dollars_to_dirhams(self):
        self.assertEqual(conversion.dollars_to_dirhams(10),100.19999999999999)
        self.assertEqual(conversion.dollars_to_dirhams(0),0)
    def test_meters_to_kilometers(self):
        self.assertEqual(conversion.meters_to_kilometers(0),0)
        self.assertEqual(conversion.meters_to_kilometers(3500),3.5)

if __name__ == "__main__":
    unittest.main()
