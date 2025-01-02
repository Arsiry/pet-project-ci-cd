"""
Script to calculate the sum of two numbers.

This script includes:
- A function to calculate the sum of two numbers.
- A function to get user input for the numbers.
- A main function to coordinate input, calculation, and output.
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


def get_user_input():
    """
    Function to get input from the user for two numbers.
    
    Returns:
    tuple: A tuple containing two numbers (float).
    """
    while True:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            return a, b
        except ValueError:
            print("Please enter valid numbers.")


def main():
    """
    Main function that supports both command-line arguments and user input.
    """
    parser = argparse.ArgumentParser(description="Calculate the sum of two numbers.")
    parser.add_argument("--num1", type=float, help="The first number")
    parser.add_argument("--num2", type=float, help="The second number")
    args = parser.parse_args()

    if args.num1 is not None and args.num2 is not None:
        # Use command-line arguments if provided
        a, b = args.num1, args.num2
    else:
        # Fall back to user input if no arguments are provided
        print("No command-line arguments provided. Switching to user input.")
        a, b = get_user_input()

    result = sum_of_two_numbers(a, b)
    print(f"The sum of {a} and {b} is {result}.")


if __name__ == "__main__":
    main()
