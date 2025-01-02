"""
Script to calculate the sum of two numbers.

This script includes:
- A function to calculate the sum of two numbers.
- Command-line argument parsing for input.
"""

import argparse

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

def main():
    """
    Main function that uses command-line arguments for input.
    """
    parser = argparse.ArgumentParser(description="Calculate the sum of two numbers.")
    parser.add_argument("--num1", type=float, required=True, help="The first number")
    parser.add_argument("--num2", type=float, required=True, help="The second number")
    args = parser.parse_args()

    # Use command-line arguments
    a, b = args.num1, args.num2

    result = sum_of_two_numbers(a, b)
    print(f"The sum of {a} and {b} is {result}.")

if __name__ == "__main__":
    main()
