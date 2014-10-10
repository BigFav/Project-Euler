from collections import deque

import numpy as np


""" Find the number of circular primes """

def primes_to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[((k*k)//3)::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]


num_circ = 0
primes = frozenset(np.char.mod('%d', primes_to(1000000)))
for prime in primes:
    is_circ_prime = True
    og_prime = prime
    prime = deque(prime)
    for _ in xrange(len(prime)):
        prime.rotate()
        num = ''.join(prime)
        if num not in primes:
            is_circ_prime = False
            break

    if is_circ_prime:
        num_circ += 1

print num_circ
