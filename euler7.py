'''
Problem 7: the 10,001st prime.
Sieve of Eratosthenes up to a safe bound (the nth prime is below n(ln n + ln ln n) for n >= 6).
'''

from math import log


def primesbelow(limit):
    '''
    Return all primes below limit by crossing out multiples of each prime.
    '''
    isprime = bytearray([1]) * limit
    isprime[0:2] = b"\x00\x00"
    for p in range(2, int(limit ** 0.5) + 1):
        if isprime[p]:
            isprime[p * p::p] = bytearray(len(range(p * p, limit, p)))
    return [i for i in range(limit) if isprime[i]]


target = 10001
bound = int(target * (log(target) + log(log(target)))) + 1
print(primesbelow(bound)[target - 1])
