'''
Problem 2: sum of the even Fibonacci numbers not exceeding four million.
Every third Fibonacci number is even, and the even ones follow e(n) = 4e(n-1) + e(n-2).
'''

limit = 4000000
previous, current = 2, 8
total = previous
'''
Walk only the even terms, so there is no need to test each number for evenness.
'''
while current <= limit:
    total += current
    previous, current = current, 4 * current + previous
print(total)
