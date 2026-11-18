'''
Problem 16: sum of the digits of 2^1000.
Python integers have no size limit, so compute the number exactly and add its digits.
'''

print(sum(int(digit) for digit in str(2 ** 1000)))
