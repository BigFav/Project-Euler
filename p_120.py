print sum(n*(n-1) if n & 1 else n*(n-2) for n in xrange(3, 1001))
