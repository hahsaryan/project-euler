'''
Problem 12: first triangular number with over 500 divisors.
T(n) = n(n+1)/2, and n and n+1 share no factors, so the divisor count splits into two smaller counts.
'''


def countdivisors(n):
    '''
    Count divisors from the prime factorization: product of (exponent + 1).
    '''
    count = 1
    factor = 2
    while factor * factor <= n:
        exponent = 0
        while n % factor == 0:
            n //= factor
            exponent += 1
        count *= exponent + 1
        factor += 1
    if n > 1:
        count *= 2
    return count


n = 1
while True:
    '''
    Halve whichever of n and n + 1 is even, then multiply the two divisor counts.
    '''
    if n % 2 == 0:
        divisors = countdivisors(n // 2) * countdivisors(n + 1)
    else:
        divisors = countdivisors(n) * countdivisors((n + 1) // 2)
    if divisors > 500:
        print(n * (n + 1) // 2)
        break
    n += 1
