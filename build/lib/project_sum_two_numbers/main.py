"""
The main function and demonstration code.
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
    by allowing user input and calculating the sum of two numbers.
    """
    try:
        # Ask user for the first number
        a = float(input("Enter the first number: "))
        # Ask user for the second number
        b = float(input("Enter the second number: "))
        # Call the function with user input, store the result in the variable result_sum
        result_sum = sum_of_two_numbers(a, b)
        # Print the result to the console
        print(f"The sum of {a} and {b} is {result_sum}")
    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    main()
