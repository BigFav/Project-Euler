from itertools import combinations

''' How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed? '''

die_pair_set = set()
dice_set = [frozenset(int(i) for i in tup) for tup in combinations('0123456789', 6)]
for die1 in dice_set:
    for die2 in dice_set:
        if (((0 in die1 and 1 in die2) or (0 in die2 and 1 in die1)) and    # 01
            ((0 in die1 and 4 in die2) or (0 in die2 and 4 in die1)) and    # 04
                ((0 in die1 and (6 in die2 or 9 in die2)) or                # 0'9'
                 (0 in die2 and (6 in die1 or 9 in die1))) and
                ((1 in die1 and (6 in die2 or 9 in die2)) or                # 1'6'
                 (1 in die2 and (6 in die1 or 9 in die1))) and
            ((2 in die1 and 5 in die2) or (2 in die2 and 5 in die1)) and    # 25
                ((3 in die1 and (6 in die2 or 9 in die2)) or                # 3'6'
                 (3 in die2 and (6 in die1 or 9 in die1))) and
                ((4 in die1 and (6 in die2 or 9 in die2)) or                # 4'9'
                 (4 in die2 and (6 in die1 or 9 in die1))) and
                (((6 in die2 or 9 in die2) and 4 in die1) or                # '6'4
                 ((6 in die1 or 9 in die1) and 4 in die2)) and
              ((8 in die1 and 1 in die2) or (8 in die2 and 1 in die1))):    # 81
            die_pair_set.add((die1, die2))

print len(die_pair_set) / 2
