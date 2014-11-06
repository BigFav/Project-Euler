from decimal import *

''' 
For the first 100 numbers, find the total of the digital sums of
the first 100 decimal digits for all the irrational square roots.
'''

def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n / 10
    return r

def isnt_perfect_square(n):
    h = n & 0xF
    if h > 9:
        return True
    if h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8:
        t = int(n**0.5)
        return t*t != n
    return True


not_squares = (i for i in xrange(2, 101) if isnt_perfect_square(i))

multiplier = 10**99
getcontext().prec = 102
print sum(sum_digits(int(Decimal(i).sqrt() * multiplier)) for i in not_squares)
