"""
Script to calculate the sum of two numbers and read from a file.

This script includes:
- A function to calculate the sum of two numbers.
- Command-line argument parsing for input.
- Reading from a file and displaying its contents.
"""

import os

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

# Function to reading from a file and displaying its content
def read_and_display_file_content(file_path):
    """
    Reads and displays the content of a given file.

    Parameters:
    file_path (str): Relative path to the file.

    Returns:
    None
    """
    # Get the absolute path to the file relative to the current script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, file_path)
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as file:
            content = file.read()
        print(content)
    else:
        print(f"File '{full_path}' not found.")

def main():
    """
    Main function
    """
    # Calculation the sum of two numbers
    a = 4
    b = 5
    result = sum_of_two_numbers(a, b)
    print(f"The sum of {a} and {b} is {result}.")

    # Reading from a file and displaying its content
    file_path = os.path.join("data", "sample.txt")
    read_and_display_file_content(file_path)

if __name__ == "__main__":
    main()
