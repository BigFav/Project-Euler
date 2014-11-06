def main1():
    string = ''.join(`num` for num in xrange(1, 185186))  # Minimized range
    print(int(string[0]) * int(string[9]) * int(string[99]) *
          int(string[999]) * int(string[9999]) * int(string[99999]) *
          int(string[999999]))

def main2():
    from math import log10
    highest_digit = 1000000
    end_digit = 10000000

    prod = 1
    curr_index = 12
    next_index = 100
    for num in xrange(11, highest_digit):
        num_len = int(log10(num)) + 1  # Stops working around 999999999999999
        distance = next_index - curr_index
        if distance < num_len:
            digits = list(`num`)
            prod *= int(digits[distance])
            next_index *= 10
            if next_index == end_digit:
                break
        curr_index += num_len
    print prod
