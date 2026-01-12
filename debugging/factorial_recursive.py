#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description:
        Computes the factorial of a non-negative integer using recursion.

    Parameter:
        n (int): The integer whose factorial is to be computed.
                 Must be greater than or equal to 0.

    Return:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
