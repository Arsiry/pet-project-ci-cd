"""
This module contains functions for calculating the sum of two numbers
and demonstrates a simple main function.
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

def main():
    """
    Main function that demonstrates the use of sum_of_two_numbers
    by calculating and printing the sum of 1 and 5.
    """
    f=6
    # Call the function with arguments 1 and 5, store the result in the variable result_sum
    result_sum = sum_of_two_numbers(1, 5)
    # Print the result to the console
    print(result_sum)

main()