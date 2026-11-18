'''
Problem 1: sum of all multiples of 3 or 5 below 1000.
Uses inclusion-exclusion on arithmetic series instead of a loop.
'''


def sumofmultiples(k, limit):
    '''
    Sum of k, 2k, 3k, ... below limit, using the arithmetic series formula.
    '''
    n = (limit - 1) // k
    return k * n * (n + 1) // 2


limit = 1000
'''
Multiples of 15 are counted in both 3 and 5, so subtract them once.
'''
total = sumofmultiples(3, limit) + sumofmultiples(5, limit) - sumofmultiples(15, limit)
print(total)
