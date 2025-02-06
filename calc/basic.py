#! /usr/bin/env python3
# Author: Lverma
# Description: This module contains
"""
 Docstrings:

 """
import sys

def add(*args):
    """  Return SUM of all parameters  """
    total = 0
    for num in args:
        total += num
    return total

def mul(*args):
    """Return PRODUCT of all parameters """
    total = 1
    for num in args:
        total *= num
    return total

def div(x, z):
    """Return QUOTIENT of x divided by z to 3 decimal places """
    if z == 0:
        return print("Division by 0!")
    else:
        return round(x/z,3)
def main():
    print(f"4 + 3 = {add(4, 3)}")
    print(f"4 + 3 + 2 = {add(4, 3, 2)}")
    print(f"4 * 3 = {mul(4, 3)}")
    print(f"4 * 3 * 2 = {mul(4, 3, 2)}")
    print(f"4 / 3 = {div(4, 0)}")
    sys.exit(0) # Exit program with 0 errors.

if __name__ == "__main__":
    main()
    sys.exit(0)