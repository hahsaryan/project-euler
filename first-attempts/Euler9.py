# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 22:36:24 2026

@author: aryan
"""

import math as m
    
i = 1
while i < 1000:
    l = i + 1
    while l < 1000:
        k = m.sqrt((i ** 2) + (l ** 2))
        if i + l + k == 1000:
            print(i * l * k)
        l += 1
    i += 1