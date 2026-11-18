# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 23:10:15 2026

@author: aryan
"""

i = 3
primes = [2]
while i < 2000000:
    l = 0
    isprime = True
    while l < len(primes) and isprime == True and primes[l] <= i ** 0.5:
        if i % primes[l] == 0:
            isprime = False
        l += 1
    if isprime == True:
        primes.append(i)
    i += 2
print(sum(primes))