"""
Script to calculate the sum of two numbers.

This script includes:
- A function to calculate the sum of two numbers.
- Command-line argument parsing for input.
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
    Main function
    """
    a = 4
    b = 5
    result = sum_of_two_numbers(a, b)
    print(f"The sum of {a} and {b} is {result}.")

if __name__ == "__main__":
    main()
