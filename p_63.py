from itertools import count
from math import log10

''' How many n-digit positive integers exist which are also an nth power? '''

answer = 0
for n in count(start=1):
    curr_incr = sum(1 for i in xrange(1, 10) if int(log10(i**n)) + 1 == n)
    answer += curr_incr
    if not curr_incr:
        break
print answer
