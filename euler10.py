'''
Problem 10: sum of all primes below two million.
Sieve of Eratosthenes: cross out multiples instead of testing each number by division.
'''


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


print(sum(primesbelow(2000000)))
