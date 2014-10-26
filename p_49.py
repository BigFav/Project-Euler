from itertools import permutations

import numpy as np

''' Find the 12-digit number of the concatenated arithemetic sequence whom are all prime. '''

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


def check_arith_seqs(og_index, prime_perms, answers):
    difference = 0
    next_index = og_index + 1
    largest_diff = (10000 - prime_perms[og_index]) / 2
    while (difference <= largest_diff) and (next_index < len(prime_perms)):
        difference = prime_perms[next_index] - prime_perms[og_index]
        potential_third = prime_perms[next_index] + difference
        next_index += 1
        if potential_third in prime_perms:
            answers.add((prime_perms[og_index]*10000 + prime_perms[next_index-1]) *
                        10000 + potential_third)
            return True
    return False


answers = set()
primes = primes_to(10000)
primes = primes[primes > 1000]
primes = frozenset(np.char.mod('%d', primes))
for prime in primes:
    prime_perms = sorted(int(x) for x in
                         {''.join(x) for x in permutations(prime)) if x in primes}
    for i in xrange(len(prime_perms) - 2):
        if check_arith_seqs(i, prime_perms, answers):
            break
    if len(answers) == 2:
        break
print answers
