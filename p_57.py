from math import log10

''' In the 1st 1000 expansions, how many fractions contain a numerator with more digits than denominator? '''

count = 0
p = q = 1
for i in xrange(999):
    p, q = p + 2*q, p + q
    if int(log10(p)) > int(log10(q)):
        count += 1
print count
