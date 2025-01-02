"""
Unit tests for the `sum_of_two_numbers` function and `get_user_input` function.

This module contains:
- A test class `TestSumOfTwoNumbers` with various test cases for the `sum_of_two_numbers` function.
- A test class `TestUserInput` with test cases for the `get_user_input` function.
"""

import unittest
from unittest.mock import patch

# Import the functions to be tested
from project_sum_two_numbers import sum_of_two_numbers
from project_sum_two_numbers import get_user_input


class TestSumOfTwoNumbers(unittest.TestCase):
    """
    Test class for the function sum_of_two_numbers.
    """

    def test_sum_of_positive_numbers(self):
        """Test for positive numbers."""
        self.assertEqual(sum_of_two_numbers(3, 7), 10)

    def test_sum_of_negative_numbers(self):
        """Test for negative numbers."""
        self.assertEqual(sum_of_two_numbers(-3, -7), -10)

    def test_sum_of_mixed_numbers(self):
        """Test for mixed positive and negative numbers."""
        self.assertEqual(sum_of_two_numbers(5, -2), 3)

    def test_sum_of_floats(self):
        """Test for floating-point numbers."""
        self.assertAlmostEqual(sum_of_two_numbers(2.5, 3.1), 5.6, places=1)

    def test_sum_with_zero(self):
        """Test for summing a number with zero."""
        self.assertEqual(sum_of_two_numbers(5, 0), 5)
        self.assertEqual(sum_of_two_numbers(0, 5), 5)

    def test_sum_large_numbers(self):
        """Test for large numbers."""
        self.assertEqual(sum_of_two_numbers(1e9, 1e9), 2e9)

    def test_sum_small_numbers(self):
        """Test for very small numbers."""
        self.assertAlmostEqual(sum_of_two_numbers(1e-10, 1e-10), 2e-10)

    def test_sum_invalid_types(self):
        """Test for invalid input types."""
        with self.assertRaises(TypeError):
            sum_of_two_numbers("a", 5)
        with self.assertRaises(TypeError):
            sum_of_two_numbers(5, None)


class TestUserInput(unittest.TestCase):
    """
    Test class for the function get_user_input.
    """

    @patch('builtins.input', side_effect=['3', '4'])
    def test_valid_input(self, mock_input):
        """Test for valid user input."""
        self.assertEqual(get_user_input(), (3.0, 4.0))

    @patch('builtins.input', side_effect=['abc', '3', '4'])
    def test_invalid_then_valid_input(self, mock_input):
        """Test for invalid input followed by valid input."""
        self.assertEqual(get_user_input(), (3.0, 4.0))

    @patch('builtins.input', side_effect=['', '3', '4'])
    def test_empty_input(self, mock_input):
        """Test for empty input."""
        self.assertEqual(get_user_input(), (3.0, 4.0))

    @patch('builtins.input', side_effect=['1.5', '2.3'])
    def test_floating_point_input(self, mock_input):
        """Test for floating-point input."""
        self.assertEqual(get_user_input(), (1.5, 2.3))

    @patch('builtins.input', side_effect=['1e5', '2e5'])
    def test_scientific_notation_input(self, mock_input):
        """Test for scientific notation input."""
        self.assertEqual(get_user_input(), (1e5, 2e5))

    @patch('builtins.input', side_effect=['1,5', '2,3'])
    def test_invalid_delimiter_input(self, mock_input):
        """Test for invalid delimiters (comma instead of dot)."""
        with self.assertRaises(ValueError):
            get_user_input()


if __name__ == "__main__":
    # Run the unit tests
    unittest.main()
