# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 00:27:19 2026

@author: aryan
"""

import math as m
i = 2
n = 600851475143
factors = []
prime = []
while i < m.sqrt(n):
    if n % i == 0:
        factors.append(i)
        factors.append(int(n/i))
    i += 1
for f in factors:
    t = 2
    l = f
    while t < m.sqrt(f):
        if f % t == 0:
            l = 0
        t += 1
    prime.append(l)
print(max(prime))