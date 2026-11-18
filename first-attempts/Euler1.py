# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 23:51:06 2026

@author: aryan
"""

count = 0
i = 1
while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        count += i
    i += 1
print(count)
