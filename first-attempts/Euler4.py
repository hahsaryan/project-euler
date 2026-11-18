# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 01:47:30 2026

@author: aryan
"""

i = 100
finnum = 0
while i < 1000:
    f = 100
    while f < 1000:
        digits = []
        t = i * f
        t = str(t)
        for c in t:
            digits.append(int(c))
        d = 0
        ispalindrome = True
        while d < int(len(digits)/2):
            if not digits[d] == digits[len(digits) - 1 - d]:
                ispalindrome = False
            d += 1
        t = int(t)
        if ispalindrome == True and t > finnum:
            finnum = t
        f += 1
    i += 1
print(finnum)