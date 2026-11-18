# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 02:31:47 2026

@author: aryan
"""
import math as m
i = 3
prime = [2]
while len(prime) < 10001:
    restart = False
    t = 0
    while t <= (len(prime) - 1) and prime[t] <= m.sqrt(i):
        if i % prime[t] == 0:
            restart = True
            break
        t += 1
    if restart == False:
        prime.append(i)
    i += 2
print(prime[10000])