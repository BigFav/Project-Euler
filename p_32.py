""" Find sum of all products whose multipiers and itself are pandigital. """

def factorize(n):
    step = (n % 2) + 1
    return sorted(x for tup in ([i, n // i] 
                  for i in xrange(1, int(n**0.5)+1, step) if n % i == 0) for x in tup)

def shares_digits(num1, num2, num3):
    digits_count = [0] * 9
    for num in [num1, num2, num3]:
        while num >= 10:
            mod_ten = num % 10
            if mod_ten == 0:
                return True
            digits_count[mod_ten - 1] += 1
            num //= 10
        digits_count[num - 1] += 1
    for digit_count in digits_count:
        if digit_count != 1:
            return True
    return False

sums = 0
for i in xrange(1234, 9787):
    factors = factorize(i)
    end_ptr = len(factors) - 1
    for beg_ptr in xrange(len(factors) // 2):
        if not shares_digits(factors[beg_ptr], factors[end_ptr], i):
            sums += i
            break
        end_ptr -= 1
print sums
