import numpy as np

""" 
Find the sum of the only eleven primes that are both truncatable
from left to right and right to left.
"""

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


num_primes = -4               # omit 2, 3, 5, 7
prime_sum = -17
primes = frozenset(primes_to(1000000))
for prime in primes:
    dividend = 10
    is_trunc_prime = True
    while dividend < prime:
        if prime % dividend not in primes or prime // dividend not in primes:
            is_trunc_prime = False
            break
        dividend *= 10

    if is_trunc_prime:
        prime_sum += prime
        num_primes += 1
        if num_primes == 11:  # Exit once we've seen all of them
            break

print prime_sum
