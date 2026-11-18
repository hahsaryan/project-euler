# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 22:03:18 2026

@author: aryan
"""

x = str(2 ** 1000)
total = 0
for number in x:
    total += int(number)
print(total)