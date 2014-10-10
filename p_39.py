""" Find perimeter size for which the number of Pythagorean triples is maximized. """

def pytrip(perim, trip=(3,4,5), prim=1):
    # Taken from: http://rosettacode.org/wiki/Pythagorean_triples#Python
    a0, b0, c0 = a, b, c = sorted(trip)
    firstprim = prim > 0
    t = set()
    while a + b + c <= perim:
        t.add((a, b, c, firstprim > 0))
        a, b, c = a+a0, b+b0, c+c0
        firstprim = False

    t2 = set()
    for a, b, c, firstprim in t:
        a2, a5, b2, b5, c2, c3, c7 = a*2, a*5, b*2, b*5, c*2, c*3, c*7
        if a5 - b5 + c7 <= perim:
            t2 |= pytrip(perim, (a - b2 + c2,  a2 - b + c2,  a2 - b2 + c3), firstprim)
        if a5 + b5 + c7 <= perim:
            t2 |= pytrip(perim, (a + b2 + c2,  a2 + b + c2,  a2 + b2 + c3), firstprim)
        if -a5 + b5 + c7 <= perim:
            t2 |= pytrip(perim, (-a + b2 + c2, -a2 + b + c2, -a2 + b2 + c3), firstprim)
    return t | t2


most_i = most_sol = 0
for i in xrange(12, 1001):
    sol = sum(1 for a,b,c,_ in pytrip(i) if a+b+c == i)
    if sol > most_sol:
        most_sol = sol
        most_i = i
print most_i
