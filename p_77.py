"""
Find the first value that can be written as the
sum of primes in over 5000 ways.
"""

not_primes = set([1])
primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23])
def is_prime(n):
    if n in primes:
        return True
    if n % 2 == 0 or n % 3 == 0 or n in not_primes:
        return False
    for i in xrange(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            not_primes.add(n)
            return False

    primes.add(n)
    return True


q = {2: [2]}
def decompose(n):
    if n in q:
        return q[n]

    if is_prime(n):
        result = [n]
    else:
        result = []
    for i in xrange(2, n):
        a = n-i
        if is_prime(a):
            R = decompose(i)
            for r in R:
                if not r or r <= a:
                    result.append(a)

    q[n] = result
    return result

i = 10
while len(decompose(i)) < 5000:
    i += 1
print i
