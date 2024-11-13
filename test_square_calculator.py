# test_square_calculator.py

import unittest
from square_calculator import SquareCalculator

class TestSquareCalculator(unittest.TestCase):

    def setUp(self):
        """This method is run before each test to set up any state."""
        self.calc = SquareCalculator()

    def test_area(self):
        """Test for the area of the square."""
        # Area of a square with side 3 should be 9
        result = self.calc.area(3)
        self.assertEqual(result, 9)

        # Area of a square with side 5 should be 25
        result = self.calc.area(5)
        self.assertEqual(result, 25)

    def test_perimeter(self):
        """Test for the perimeter of the square."""
        # Perimeter of a square with side 3 should be 12
        result = self.calc.perimeter(3)
        self.assertEqual(result, 12)

        # Perimeter of a square with side 5 should be 20
        result = self.calc.perimeter(5)
        self.assertEqual(result, 20)

if __name__ == '__main__':
    unittest.main()
