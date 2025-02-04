#! /usr/bin/env python3
# Author: Lverma
# Description: This script will demo HOWTO repeat a block of
# commands a specific number of times using a COUNTER loop.
"""
    Docstring:
"""
count = 0 # 1.Intiatilise counter
while count < 10: # 2. Test counter
    print(count)
    count += 1
# Alternatively, we could user a FOR loop plus the built-in
# range(start, stop, step) function.
for num in range(0,11,2):
    print(num)

for num in range(0,10):
    print(num)

for num in range(10):
    print(num)

