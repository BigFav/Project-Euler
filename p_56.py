''' For a^b, where a, b < 100, what is the maximum digital sum? '''

def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n / 10
    return r

print max(max(sum_digits(a**b) for b in xrange(1, 100)) for a in xrange(1, 100))
