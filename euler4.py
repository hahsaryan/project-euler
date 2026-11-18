'''
Problem 4: largest palindrome made from the product of two 3-digit numbers.
Searches from the top down and stops early once no larger product is possible.
'''


def ispalindrome(number):
    '''
    A number is a palindrome if its digits read the same reversed.
    '''
    text = str(number)
    return text == text[::-1]


best = 0
for a in range(999, 99, -1):
    '''
    If even a * 999 cannot beat the best found, no smaller a can either.
    Start b at a to avoid checking each pair twice.
    '''
    if a * 999 <= best:
        break
    for b in range(999, a - 1, -1):
        product = a * b
        if product <= best:
            break
        if ispalindrome(product):
            best = product
print(best)
