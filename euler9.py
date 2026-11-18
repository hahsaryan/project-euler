'''
Problem 9: the Pythagorean triplet with a + b + c = 1000; print abc.
Fixes a and b, sets c = 1000 - a - b, and checks with exact integer math (no square roots).
'''

total = 1000
for a in range(1, total // 3):
    for b in range(a + 1, (total - a) // 2 + 1):
        c = total - a - b
        if a * a + b * b == c * c:
            print(a * b * c)
