# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 02:24:54 2026

@author: aryan
"""

i = 2
lenseq = 0
while i < 1000000:
    sequence = [i]
    l = i
    while l != 1:
        if l % 2 == 0:
            l = l / 2
            sequence.append(l)
        else:
            l = (3 * l) + 1
            sequence.append(l)
    if len(sequence) > lenseq:
        lenseq = len(sequence)
        number = i
    i += 1
print(number)