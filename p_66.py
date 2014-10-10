""" Find the n with the largest minimum x solution in Pell's equation. """

# http://en.wikipedia.org/wiki/Chakravala_method
def chakravala(N):
    a = int(round(N**0.5))
    b = 1
    k = a*a - N
    while a*a - N*b*b != 1:
        abs_k = abs(k)
        og_m = 1
        while (a + b*og_m) % abs_k:
            og_m += 1

        t = 2
        m = og_m
        m_sq = m * m
        next_m = abs_k + og_m
        next_m_sq = next_m * next_m
        while abs(m_sq - N) > abs(next_m_sq - N):
            m = next_m
            m_sq = next_m_sq
            next_m = abs_k*t + og_m
            next_m_sq = next_m * next_m
            t += 1

        a, b = (a*m + N*b) / abs_k, (a + b*m) / abs_k
        k = (m*m - N) / k
    return a

max_a = max_D = 0
perfect_squares = {n*n for n in xrange(100)}
for i in xrange(61, 1000):
    if i not in perfect_squares:
        a = chakravala(i)
        if a > max_a:
            max_a = a
            max_D = i
print max_D, max_a
