from fractions import Fraction
from operator import mul

""" Find the denominator for the product of digit cancelling fractions. """

digit_cancel_fracs = []
for numerator in xrange(10, 99):
    if numerator % 10 == 0 or numerator % 11 == 0:  # trivial cases
        continue

    for denominator in xrange(numerator + 1, 100):
        real_frac = Fraction(numerator, denominator)
        
        # check if numbers share digits
        num_digits = list(`numerator`)
        den_digits = list(`denominator`)
        if den_digits[0] in num_digits:
            num_digits.remove(den_digits[0])
            del den_digits[0]
        elif den_digits[1] in num_digits:
            num_digits.remove(den_digits[1])
            del den_digits[1]
        else:
            continue
        
        if int(den_digits[0]) != 0 and real_frac == Fraction(int(num_digits[0]), int(den_digits[0])):
            digit_cancel_fracs.append(real_frac)
            if len(digit_cancel_fracs) == 4:
                break

print reduce(mul, digit_cancel_fracs, 1)
