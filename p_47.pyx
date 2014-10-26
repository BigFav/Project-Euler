cimport cython
from cpython cimport bool

''' Find the first of the first four consecutive integers to have four distinct prime factors. '''

@cython.boundscheck(False)
@cython.wraparound(False)
cdef bool four_prime_factors(int n):
    cdef int d = 2
    cdef set prime_fac = set()
    while d*d <= n:
        while (n % d) == 0:
            prime_fac.add(d)
            n /= d
        d += 1
    if n > 1:
        prime_fac.add(n)
    return len(prime_fac) > 3

def main():
    cdef int first = 644
    while True:
        while not four_prime_factors(first):
            first += 1

        if not four_prime_factors(first+1):
            first += 2
            continue
        if not four_prime_factors(first+2):
            first += 3
            continue
        if not four_prime_factors(first+3):
            first += 4
            continue
        break
    print first
