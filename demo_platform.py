#! /usr/bin/env python3
# Author: Lverma
# Description: This script will demo
"""
    Docstring:
"""
import os
import sys

if sys.platform == "win32":
    home_dir = os.environ["HOMEPATH"]
else:
    home_dir = os.environ["HOME"]

print(home_dir)