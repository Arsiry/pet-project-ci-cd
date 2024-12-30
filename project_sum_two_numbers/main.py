#!/bin/python

"""
Script to calculate the sum of two numbers.

This script includes:
- A function to calculate the sum of two numbers.
- A function to get user input for the numbers.
- A main function to coordinate input, calculation, and output.
"""


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
    Main function that demonstrates the use of sum_of_two_numbers
    by allowing user input and calculating the sum of two numbers.
    """
    result = sum_of_two_numbers(2, 3)
    print(f"The sum of {result}")


if __name__ == "__main__":
    main()
