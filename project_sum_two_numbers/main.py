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

def read_file():
    """
    Reads and returns the content of the sample.txt file.

    Returns:
    str: Content of the file.
    """
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'sample.txt')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."

def main():
    """
    Main function
    """
    # Calculation of the sum of two numbers
    a = 4
    b = 5
    result = sum_of_two_numbers(a, b)
    print(f"The sum of {a} and {b} is {result}.")

    # Reading and printing the content of the file
    file_content = read_file()
    print(f"Content of the file:\n{file_content}")

if __name__ == "__main__":
    main()
