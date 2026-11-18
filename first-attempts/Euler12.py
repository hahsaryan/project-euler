# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 23:49:11 2026

@author: aryan
"""

import math as m

i = 1
divisors = []
trinum = 0
while len(divisors) < 500:
    trinum += i
    l = 1
    divisors = []
    while l <= m.sqrt(trinum):
        if trinum % l == 0:
            divisors.append(l)
            if trinum / l != l:
                divisors.append(trinum/l)
        l += 1
    i += 1
print(trinum)