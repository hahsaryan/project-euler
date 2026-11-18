'''
Problem 14: starting number under one million with the longest Collatz chain.
Memoization: store each chain length so later chains stop as soon as they reach a known number.
'''

limit = 1000000
lengths = [0] * limit
lengths[1] = 1


def collatzlength(start):
    '''
    Follow the chain until it hits a number whose length is already stored,
    then fill in the lengths of every number visited on the way.
    '''
    path = []
    n = start
    while n >= limit or lengths[n] == 0:
        path.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    length = lengths[n]
    for value in reversed(path):
        length += 1
        if value < limit:
            lengths[value] = length
    return lengths[start]


best = max(range(1, limit), key=collatzlength)
print(best)
