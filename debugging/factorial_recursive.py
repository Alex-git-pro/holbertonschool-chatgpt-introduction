#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer recursively.

    Function Description:
    This function computes the factorial of a given non-negative integer `n` using recursion. 
    The factorial of a number is the product of all positive integers less than or equal to the number.
    Special case: The factorial of 0 is defined as 1.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input number `n`.
    """
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n-1)  # Recursive case: n * factorial of (n-1)

if __name__ == "__main__":
    # Read an integer from command-line arguments
    f = factorial(int(sys.argv[1]))
    # Print the factorial result
    print(f)
