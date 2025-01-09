"""
Unit tests for the `sum_of_two_numbers` function and `read_and_display_file_content`.

This module contains:
- A test class `TestSumOfTwoNumbers` with various test cases for the `sum_of_two_numbers` function.
- A test class `TestReadAndDisplayFileContent` for the `read_and_display_file_content` function.
"""

import unittest
#from unittest.mock import patch, mock_open
#from io import StringIO
#import os


# Import the function to be tested
from project_sum_two_numbers import sum_of_two_numbers#, read_and_display_file_content
#from project_sum_two_numbers.main import main


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


#class TestReadAndDisplayFileContent(unittest.TestCase):
#    """
#    Test class for the function read_and_display_file_content.
#    """
#    @patch("builtins.open", new_callable=mock_open, read_data="Sample file content")
#    @patch("os.path.exists", return_value=True)
#    def test_read_and_display_file_content(self, _, __):
#        """Test reading from a file and displaying its content."""
#        with patch("sys.stdout", new=StringIO()) as mock_stdout:
#            read_and_display_file_content("dummy_path.txt")
#            self.assertIn("Sample file content", mock_stdout.getvalue())
#
#    @patch("os.path.exists", return_value=False)
#    def test_file_not_found(self, _):
#        """Test handling when the file is not found."""
#        with patch("sys.stdout", new=StringIO()) as mock_stdout:
#            read_and_display_file_content("dummy_path.txt")
#            self.assertIn("File '", mock_stdout.getvalue())
#            self.assertIn("not found.", mock_stdout.getvalue())


#class TestMainFunction(unittest.TestCase):
#    """
#    Test class for the main function.
#    """
#    @patch("project_sum_two_numbers.main.read_and_display_file_content")
#    @patch("sys.stdout", new_callable=StringIO)
#    def test_main(self, mock_stdout, mock_read_file):
#        """Test the main function output."""
#        main()
#        self.assertIn("The sum of 4 and 5 is 9.", mock_stdout.getvalue())
#        mock_read_file.assert_called_once_with(os.path.join("data", "sample.txt"))


if __name__ == "__main__":
    # Run the unit tests
    unittest.main()
