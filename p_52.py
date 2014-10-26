from itertools import count
from math import log10

''' Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits. '''

for i in count(start=10):
    sorted_str_num = sorted(`i`)
    num_len = len(sorted_str_num) - 1

    # Check lengths
    nums = (6*i, 5*i, 4*i, 3*i, 2*i)
    if (num_len == int(log10(nums[0])) == int(log10(nums[1])) ==
        int(log10(nums[2])) == int(log10(nums[3])) == int(log10(nums[4]))):
        # Check if numbers are equal
        if (sorted_str_num == sorted(`nums[0]`) == sorted(`nums[1]`) ==
            sorted(`nums[2]`) == sorted(`nums[3]`) == sorted(`nums[4]`)):
            break
print i
