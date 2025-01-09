"""
Unit tests for the `sum_of_two_numbers` function and `read_file`.

This module contains:
- A test class `TestSumOfTwoNumbers` with various test cases for the `sum_of_two_numbers` function.
- A test class `TestReadFile` with various test cases for the `read_file` function.
"""

import unittest
from unittest.mock import patch, mock_open
import io
import os

# Import the functions to be tested
from project_sum_two_numbers.main import sum_of_two_numbers, read_file


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


class TestReadFile(unittest.TestCase):
    """
    Test class for the function read_file.
    """

    @patch("builtins.open", new_callable=mock_open, read_data="Hello world!")
    def test_read_file_success(self, mock_file):
        """Test successful reading of the file."""
        expected_content = "Hello world!"
        file_path = os.path.join(os.path.dirname(__file__), 'data', 'sample.txt')

        # Mock os.path.join to return a fixed file path
        with patch("os.path.join", return_value=file_path):
            content = read_file()
            self.assertEqual(content, expected_content)

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_file):
        """Test handling of a missing file."""
        with patch("os.path.join", return_value="nonexistent_file.txt"):
            content = read_file()
            self.assertEqual(content, "File not found.")


class TestMainFunction(unittest.TestCase):
    """
    Test class for the main function.
    """

    @patch("builtins.open", new_callable=mock_open, read_data="Hello world!")
    @patch("project_sum_two_numbers.main.sum_of_two_numbers", return_value=9)
    def test_main_output(self, mock_sum, mock_file):
        """Test main function output."""
        expected_output = "The sum of 4 and 5 is 9.\nContent of the file:\nHello world!\n"

        # Capture output
        with patch("sys.stdout", new=io.StringIO()) as fake_output:
            unittest.main()
            self.assertEqual(fake_output.getvalue(), expected_output)


if __name__ == "__main__":
    # Run the unit tests
    unittest.main()
