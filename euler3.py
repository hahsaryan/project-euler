'''
Problem 3: largest prime factor of 600851475143.
Divides out each factor as soon as it is found, so no separate primality test is needed.
'''

n = 600851475143
factor = 2
largest = 1
'''
Any factor found this way is prime, because all smaller factors were already removed.
Stop once factor squared exceeds what is left; the leftover is itself prime.
'''
while factor * factor <= n:
    while n % factor == 0:
        largest = factor
        n //= factor
    factor += 1 if factor == 2 else 2
if n > 1:
    largest = n
print(largest)
