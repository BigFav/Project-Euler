from math import factorial

''' Find sum of factorians. '''

factorial_list = [factorial(n) for n in xrange(10)]

def fac_equals_digits(n):
    fac_sum = 0
    n_copy = n
    while n >= 10:
        fac_sum += factorial_list[n % 10]
        n //= 10
    return fac_sum + factorial_list[n] == n_copy

fac_sum = 0
for i in xrange(10, 100000):
    if fac_equals_digits(i):
        fac_sum += i
print fac_sum
