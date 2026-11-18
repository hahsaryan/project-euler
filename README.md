# Project Euler Solutions (Python)

My solutions to [Project Euler](https://projecteuler.net) problems. The main folder holds refined solutions; `first-attempts/` keeps my original brute-force versions so the improvement is visible.

Run any solution with `python euler10.py`.

## Solutions

| Problem | Topic | Refined approach |
| --- | --- | --- |
| 1 | Multiples of 3 or 5 | Inclusion-exclusion with the arithmetic series formula |
| 2 | Even Fibonacci numbers | Generates only the even terms: e(n) = 4e(n-1) + e(n-2) |
| 3 | Largest prime factor | Divides out factors as found, so no primality test is needed |
| 4 | Largest palindrome product | Top-down search with early stopping |
| 5 | Smallest multiple | LCM of 1-20 via gcd |
| 6 | Sum square difference | Closed-form formulas for both sums |
| 7 | 10,001st prime | Sieve of Eratosthenes up to a proven bound on the nth prime |
| 8 | Largest product in a series | Sliding window with `math.prod` |
| 9 | Special Pythagorean triplet | Exact integer check with c = 1000 - a - b |
| 10 | Summation of primes | Sieve of Eratosthenes |
| 11 | Largest product in a grid | Direction vectors over a 2D grid |
| 12 | Highly divisible triangular number | T(n) = n(n+1)/2 with coprime n and n+1; divisor counts from prime factorization |
| 13 | Large sum | Exact big-integer sum, first ten digits |
| 14 | Longest Collatz sequence | Memoized chain lengths |
| 16 | Power digit sum | Exact big-integer arithmetic |

## Speedups from refining

| Problem | First attempt | Refined | Faster by |
| --- | --- | --- | --- |
| 10 | 5.8 s (trial division) | 0.07 s (sieve) | about 80x |
| 12 | 5.3 s (divisor search per number) | 0.06 s (factorization of n and n+1) | about 90x |
| 14 | 15.8 s (full simulation of every chain) | 0.42 s (memoization) | about 38x |

Timings on one machine; your numbers will differ but the ratios should be similar.

## Fixes from the first attempts

- Problem 5: the first attempt never stopped looping after printing the answer.
- Problem 9: replaced a floating-point square-root comparison with an exact integer check.
- Problem 13: prints the first ten digits, as the problem asks, instead of the whole sum.
