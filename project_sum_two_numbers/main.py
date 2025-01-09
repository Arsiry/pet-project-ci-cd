"""
Script to calculate the sum of two numbers and read from a file.

This script includes:
- A function to calculate the sum of two numbers.
- Command-line argument parsing for input.
- Reading from a file and displaying its contents.
"""

import os
import importlib.resources

# Function to calculate the sum of two numbers
def sum_of_two_numbers(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.

    Returns:
    int, float: The sum of a and b.
    """
    return a + b

# Function to read from a file and display its content
def read_and_display_file_content_from_package():
    """
    Reads and displays the content of 'sample.txt' from the package.

    Returns:
    None
    """
    try:
        # Use importlib.resources to open the file from the package
        with importlib.resources.open_text('project_sum_two_numbers.data', 'sample.txt') as file:
            content = file.read()
        print(content)
    except FileNotFoundError:
        print("File 'sample.txt' not found in the package.")


def main():
    """
    Main function
    """
    # Calculation the sum of two numbers
    a = 4
    b = 5
    result = sum_of_two_numbers(a, b)
    print(f"The sum of {a} and {b} is {result}.")

    # Read and display file content from the package
    read_and_display_file_content_from_package()

if __name__ == "__main__":
    main()
