#! /usr/bin/env python3
# Author: Lverma
# Description: This script will simulate a high street bank
# ATM PIN machine.
"""
    Docstring:
"""
master_pin ="0123"
pin = None

# Loop whilst PIN is incorrect
attempts = 0
while pin != master_pin and attempts < 3:
    pin = input ("Enter PIN: ")
    if pin == master_pin:
        print("Valid PIN")
        break
    else:
        print("Invalid PIN")
        attempts += 1
else:
    print("Max attempts reached. Please try again later")

print("Done.")