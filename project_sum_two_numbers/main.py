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
    result = a + b
    return result

def main():
    """
    Main function
    """
    print(f"The sum of 4 and 5 is {sum_of_two_numbers(4, 5)}.")

if __name__ == "__main__":
    main()
