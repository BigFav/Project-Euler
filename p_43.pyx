from itertools import permutations

cimport cython
from cpython cimport bool

''' Find sum of pandigitals whose nth 3 digit slices are divisible by the nth prime. '''

@cython.boundscheck(False)
@cython.wraparound(False)
def main():
    answer = 0
    cdef bool is_divisible
    cdef int *div_nums = [2, 3, 5, 7, 11, 13, 17]
    for perm in (''.join(i) for i in permutations('0123456789')):
        is_divisible = True
        for i in xrange(1, 8):
            if int(perm[i:i+3]) % div_nums[i-1]:
                is_divisible = False
                break
        if is_divisible:
            answer += int(perm)
    print answer
