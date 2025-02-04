#! /usr/bin/env python3
# Author: Lverma
# Description: This script will demo HOWTO split and rejoin strings
"""
    Docstring:
"""

line = "root:x:0:0:The Super User:/root:/bin/ksh"

print(line)
# AND I want to MODIFY the strings
fields = line.split(":")
fields[4] = "The Administrator"
fields[6] = "/bin/bash"
line = ":".join(fields)

print(fields)
print(line)