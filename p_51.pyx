from itertools import permutations

import numpy as np
cimport numpy as np
cimport cython

'''
Find the smallest prime which, by replacing part of the number
with the same digit, is part of an eight prime value family.
'''

@cython.boundscheck(False)
@cython.wraparound(False)
cdef np.ndarray primes_to(int n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    cdef int k
    cdef np.ndarray sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[((k*k)//3)::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

def main():
    cdef str stars = '*'
    cdef int beg = 10000
    cdef int end = 100000
    cdef int low = 1000000
    cdef set indices_memo = set()
    cdef frozenset even = frozenset(['0', '2', '4', '6', '8', '*'])

    cdef np.ndarray all_primes = primes_to(low)
    all_primes = all_primes[all_primes >= end]
    cdef frozenset primes = frozenset(all_primes)

    cdef set perms
    cdef str perm_num, i_str, tmp
    cdef int num_in, tmp_low, num, q
    for q in xrange(4):
        for i in xrange(beg, end):
            i_str = `i`
            perm_num = ''.join(sorted(i_str))
            if perm_num in indices_memo:
                continue
            indices_memo.add(perm_num)

            perms = {''.join(x) for x in permutations(stars + i_str) if x[-1] not in even and x[0] != '0'}
            for perm in perms:
                num_in = 0
                tmp_low = 1000000
                for star in xrange(10):
                    tmp = perm.replace('*', `star`)
                    num = int(tmp)
                    if num in primes:
                        num_in += 1
                        if num < tmp_low:
                            tmp_low = num

                if num_in == 8 and tmp_low < low:
                    low = tmp_low
        beg /= 10
        end /= 10
        stars += '*'
    print low
