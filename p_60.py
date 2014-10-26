from collections import defaultdict
from copy import copy
from math import log10

import numpy as np

''' Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime. '''

def int_concat(x, y):
    a = int(log10(y)) + 1
    return int(x*10**a+y)

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


primes = primes_to(100000000)
primes_set = frozenset(primes)
iter_primes = primes[primes < 10000]

# Fill in dict
concat_primes = defaultdict(set)
for prime in iter_primes:
    for cc_prime in iter_primes:
        if (int_concat(prime, cc_prime) in primes_set and
                int_concat(cc_prime, prime) in primes_set and prime != cc_prime):
            concat_primes[prime].add(cc_prime)

concat_primes = {k: v for k, v in concat_primes.iteritems() if len(v) >= 4}
for prime, concat_set in concat_primes.iteritems():
    concat_primes[prime] = {prime for prime in concat_set if prime in concat_primes}

min_prime_sum = float('inf')
for prime1, set1 in concat_primes.items():
    if prime1 > min_prime_sum:
        continue

    for prime2 in set1:
        concat_primes[prime2].discard(prime1)
        prime2_sum = prime1 + prime2
        if prime2_sum > min_prime_sum:
            continue

        for prime3 in concat_primes[prime2]:
            prime3_sum = prime2_sum + prime3
            if prime3_sum > min_prime_sum:
                continue

            set3 = copy(concat_primes[prime3])
            if prime1 not in set3:
                continue
            set3.discard(prime1)
            set3.discard(prime2)

            for prime4 in set3:
                prime4_sum = prime3_sum + prime4
                if prime4_sum > min_prime_sum:
                    continue

                set4 = copy(concat_primes[prime4])
                if prime1 not in set4 or prime2 not in set4:
                    continue
                set4.discard(prime1)
                set4.discard(prime2)
                set4.discard(prime3)

                for prime5 in set4:
                    prime_sum = prime4_sum + prime5
                    if prime_sum < min_prime_sum:
                        set5 = concat_primes[prime5]
                        if (prime1 not in set5 or prime2 not in set5 or
                                prime3 not in set5):
                            continue
                        min_prime_sum = prime_sum
print min_prime_sum
