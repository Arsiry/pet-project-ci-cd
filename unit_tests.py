"""
Unit tests for the `sum_of_two_numbers` function.

This module contains:
- A test class `TestSumOfTwoNumbers` with various test cases for the `sum_of_two_numbers` function.
"""

import unittest


# Import the function to be tested
from project_sum_two_numbers import sum_of_two_numbers

class TestSumOfTwoNumbers(unittest.TestCase):
    """
    Test class for the function sum_of_two_numbers.
    """
    def test_positive_numbers(self):
        """Test the sum of two positive numbers."""
        self.assertEqual(sum_of_two_numbers(3, 5), 8)

    def test_negative_numbers(self):
        """Test the sum of two negative numbers."""
        self.assertEqual(sum_of_two_numbers(-3, -5), -8)

    def test_mixed_numbers(self):
        """Test the sum of one positive and one negative number."""
        self.assertEqual(sum_of_two_numbers(10, -4), 6)

    def test_zero(self):
        """Test the sum of a number and zero."""
        self.assertEqual(sum_of_two_numbers(7, 0), 7)
        self.assertEqual(sum_of_two_numbers(0, 7), 7)

    def test_floats(self):
        """Test the sum of two floating-point numbers."""
        self.assertAlmostEqual(sum_of_two_numbers(3.5, 2.1), 5.6)


if __name__ == "__main__":
    # Run the unit tests
    unittest.main()
