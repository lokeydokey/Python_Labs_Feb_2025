#! /usr/bin/env python3
# Author: Lverma
# Description: This module contains a collection of advance calc functions
""" 
 Advance calc functions including mod, power, and sqrt:
 
 """
import sys

def mod(x, z):
    """ Return remainder of x divided by z """
    if z == 0:
        return print("Division by 0!")
    else:
        return x % z

def power ( x, z):
    return x**z

def sqrt(x):
    return round(x**0.5,2)


print("ADVANCED Calculator App")
print("_" * 30)

print (f"100 % 30 = {mod (100, 30)}")
print(f"100 ** 3 = {power(100, 3)}")
print(f"\N{square root}100 = {sqrt(100)}")

sys.exit(0)