#! /usr/bin/env python3
# Author: Lverma
# Description: This script will demo
"""
    Docstring:
"""
import re
all_ports = set (range(1,201))
used_ports = set()

filepath = "C:\Windows\System32\drivers\etc\services"

with open(filepath,"rt") as file:
    for line in file:
        m = re.search(r"(\d+)/(tcp|udp)", line)
        if m:
            port = int(m.group(1))
            used_ports.add(port)

print(f"{all_ports}")
print(f"{used_ports}")
print("Unused port",f"{all_ports - used_ports}")