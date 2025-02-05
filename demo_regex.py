#! /usr/bin/env python3
# Author: Lverma
# Description: This script will demo
"""
    Docstring:
"""
import re

# Open File handle for READING in TEXT mode
fh_in = open(r"c:/labs/words", mode="rt")
i = 0
for line in fh_in:
    # if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
    # m = re.search("the", line)
    # m = re.search("^the", line)
    # m = re.search("ing$", line)
    # m = re.search("^ring$", line)
    # m = re.search("^.ing$", line)
    # m = re.search("^...................$", line)
    # m = re.search("\.", line)
    # m = re.fullmatch("^{4}", line)
    m = re.search(r"^(.)(.).\2\1$", line)
    if m:
        i += 1
        print(line, end="")
print("Total number of findings", i)