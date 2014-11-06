''' Find the last ten digits of the prime number 28433×2^(7830457)+1. '''
print (28433 * pow(2, 7830457, 10**10) + 1) % 10**10
