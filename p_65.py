''' Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e. '''

def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n / 10
    return r

mid_conv = 4
h_old = 8; h = 11
for i in xrange(3, 99, 3):
    tmp = h + h_old
    h_old = mid_conv*tmp + h
    h = tmp + h_old
    mid_conv += 2
print sum_digits(h), h
