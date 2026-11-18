# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 00:02:17 2026

@author: aryan
"""

count = 1
temp = 1
i = 2
sumcnt = 0
while i < 4000000:
    if i % 2 == 0:
        sumcnt += i
    temp = count
    count = i
    i += temp
print(sumcnt)