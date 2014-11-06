from itertools import permutations

""" Find largest pandigital prime that exits (n < 10). """

def is_prime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in xrange(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


number_str = '987654321'
pandigitals = filter(is_prime, (int(''.join(i)) for i in permutations(number_str)))
while not pandigitals:
    number_str = number_str[1:]
    pandigitals = filter(is_prime, (int(''.join(i)) for i in permutations(number_str)))
print pandigitals[0]
