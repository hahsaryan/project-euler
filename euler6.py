'''
Problem 6: difference between the square of the sum and the sum of the squares of 1..100.
Both parts have closed-form formulas, so no loop is needed.
'''

n = 100
squareofsum = (n * (n + 1) // 2) ** 2
sumofsquares = n * (n + 1) * (2 * n + 1) // 6
print(squareofsum - sumofsquares)
