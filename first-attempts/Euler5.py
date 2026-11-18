# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 02:06:21 2026

@author: aryan
"""

i = 1
divby = 16 * 9 * 5 * 7 * 11 * 13 * 17 * 19
print(divby)
while not (i % divby) + 1 == 0:
    if i % divby == 0:
        print(i)
    i += 1