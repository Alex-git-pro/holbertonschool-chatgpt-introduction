#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Fix: Decrement n to prevent infinite loop
    return result

if __name__ == "__main__":
    try:
        # Parse input argument
        n = int(sys.argv[1])
        # Ensure non-negative input
        if n < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            f = factorial(n)
            print(f)
    except (IndexError, ValueError):
        print("Usage: ./factorial.py <non-negative integer>")
