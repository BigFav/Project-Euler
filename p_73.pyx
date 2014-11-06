''' How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000? '''

cdef int gcd(int a, int b):
    while b:
        a, b, = b, a % b
    return a

def main():
    cdef:
        int simplify
        int numer, denom
        set frac_set = set()
    for denom in xrange(6000, 12001):
        for numer in xrange(denom//3 + 1, denom//2 + 1):
            simplify = gcd(numer, denom)
            frac_set.add((numer//simplify, denom//simplify))

    print(len(frac_set)) - 1 # 1/2 will be in
