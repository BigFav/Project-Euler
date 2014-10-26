import numpy as np

''' Which prime, below one-million, can be written as the sum of the most consecutive primes? '''

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


primes = primes_to(1000000)
primes_set = frozenset(primes)
primes = primes[4057:2:-1].tolist()  # reversed to avoid pop(0)
size = num = max_size = partial_sum = 0
while partial_sum < 1000000: 
    prime_iterator = reversed(primes)
    for prime in prime_iterator:
        partial_sum += prime
        if partial_sum >= 1000000:
            break
        if size > max_size and partial_sum in primes_set:
            max_size = size
            num = partial_sum

        partial_sum += prime_iterator.next()
        size += 2

    size = max_size
    partial_sum = num - primes.pop() + primes[max_size+2]
print num, max_size
