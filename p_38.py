""" Find largest 9-digit pandigital number, formed through concated products. """

def is_pandigital(num):
    digit_counts = [0] * 9
    for digit in num:
        digit = int(digit) - 1
        if digit_counts[digit] != 0:
            return False
        digit_counts[digit] = 1
    return True


num = 11
max_pan = 918273645
while num < 10000:  # arbitrarily large number
    n = 1
    prod_len = 0
    concat_prod = ''
    while prod_len < 10:
        prod = num * n
        concat_prod += `prod`
        prod_len = len(concat_prod)
        if prod_len == 9 and is_pandigital(concat_prod):
            if concat_prod > max_pan:
                max_pan = concat_prod
            break
        n += 1
    num += 2
print max_pan
