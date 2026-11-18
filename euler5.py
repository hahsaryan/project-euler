'''
Problem 5: smallest number evenly divisible by every number from 1 to 20.
That is the least common multiple of 1..20, built up one number at a time with gcd.
'''

from math import gcd

lcm = 1
for k in range(1, 21):
    '''
    lcm(a, b) = a * b / gcd(a, b)
    '''
    lcm = lcm * k // gcd(lcm, k)
print(lcm)
