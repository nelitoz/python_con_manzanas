import unittest
import calculator
from math import pi

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        expected_result = 10
        result = calculator.add(5,5)
        self.assertEqual(expected_result, result)        
    def test_area_of_circle(self):
        expected_result = pi
        result = calculator.area_of_circle(1)
        self.assertAlmostEqual(expected_result, result) 
    def test_area_of_circle_negative(self):
        self.assertRaises(ValueError, calculator.area_of_circle, -1)
if __name__=="__main__":
    unittest.main()   
