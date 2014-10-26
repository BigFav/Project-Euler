import numpy as np

''' Find the smallest odd composite that cannot be written as the sum of a prime and twice a square. '''

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


sums = set()
primes_lst = primes_to(1000000)
primes_set = frozenset(primes_lst)
for i in xrange(1000):
    for d in xrange(100):
        val = primes_lst[i] + 2*d*d
        if val % 2 != 0 and val not in primes_set:
            sums.add(val)

last_value = 7
break_flag = False
for value in sorted(sums):
    for num in xrange(last_value+2, value):
        if num % 2 != 0 and num not in primes_set:
            break_flag = True
            break
    last_value = value
    if break_flag:
        break
print num
