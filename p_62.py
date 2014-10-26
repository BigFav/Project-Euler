from collections import defaultdict
from itertools import count

''' Find the smallest cube for which exactly five permutations of its digits are cube. '''

cube_og_nums = {}
cube_perms = defaultdict(int)
for cube in (i**3 for i in count(start=346)):
    sorted_num = int("".join(sorted(`cube`)))
    cube_perms[sorted_num] += 1
    if sorted_num not in cube_og_nums:
        cube_og_nums[sorted_num] = cube
    if cube_perms[sorted_num] == 5:
        break
print cube_og_nums[sorted_num]
