#! /usr/bin/env python3
# Author: Lverma
# Description: This script will demo
"""
    Docstring:
"""

import random

lotto = []
win_lotto = [36,34,6,18,24]

while lotto != win_lotto:
    lotto = []
    while len(lotto) <5:
        num = random.randint (1,50)
        if num not in lotto:
            lotto.append(num)
#        else:
#            print("Duplicate number", num)
    print("Lottery number =", lotto)

print("##%$#$%##%##%##$#$ JACKPOT! You are winner #$#%#$%#$%#$#$#$", win_lotto)



