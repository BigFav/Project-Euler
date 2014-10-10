""" Find number of ways double pound coin using any number of coins. """

coin_nums = frozenset([1, 2, 5, 10, 20, 50, 100, 200])
p = {1: [1]}
def decomp(n):
    if n in p:
        return p[n]

    if n in coin_nums:
        result = [n]
    else:
        result = []
    for i in xrange(1, n):
        a = n-i
        if a in coin_nums:
            R = decomp(i)
            for r in R:
                if not r or r <= a:
                    result.append(a)
    p[n] = result
    return result

print len(decomp(200))
