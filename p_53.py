#from sympy import binomial
from math import factorial  # Strangely fast!

''' How many, not necessarily distinct, values of nCr, for 1 ≤ n ≤ 100, are greater than 1000000? '''

num_millies = 0
for n in xrange(23, 101):
    for r in xrange(4, n//2 + 1):
        if factorial(n) // (factorial(r)*factorial(n-r)) > 1000000:
            num_millies += n - 2*r + 1
            break
print num_millies
