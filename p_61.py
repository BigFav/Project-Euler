from copy import copy

''' Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type. '''

triangles = [n*(n+1) // 2 for n in xrange(45, 141)]
squares = [n*n for n in xrange(32, 100)]
pentagonals = [n*(3*n-1) // 2 for n in xrange(26, 82)]
hexagonals = [n*(2*n-1) for n in xrange(23, 71)]
heptagonals = [n*(5*n-3) // 2 for n in xrange(21, 64)]
octagonals = (n*(3*n-2) for n in xrange(19, 59))
remains = [heptagonals, hexagonals, pentagonals, squares, triangles]

def main():
    last_digits = 0
    bot_eq_top = lambda x: x // 100 == last_digits
    for octs in octagonals:
        for lst in remains:
            re_copy = copy(remains)
            re_copy.remove(lst)
            last_digits = octs % 100
            for poly2 in filter(bot_eq_top, lst):
                for lst2 in re_copy:
                    re_copy2 = copy(re_copy)
                    re_copy2.remove(lst2)
                    last_digits = poly2 % 100
                    for poly3 in filter(bot_eq_top, lst2):
                        for lst3 in re_copy2:
                            re_copy3 = copy(re_copy2)
                            re_copy3.remove(lst3)
                            last_digits = poly3 % 100
                            for poly4 in filter(bot_eq_top, lst3):
                                for lst4 in re_copy3:
                                    re_copy4 = copy(re_copy3)
                                    re_copy4.remove(lst4)
                                    last_digits = poly4 % 100
                                    for poly5 in filter(bot_eq_top, lst4):
                                        for lst5 in re_copy4:
                                            last_digits = poly5 % 100
                                            for poly6 in filter(bot_eq_top, lst5):
                                                if poly6 % 100 == octs // 100:
                                                    return (octs+poly2+poly3+poly4+poly5+poly6,
                                                            octs,poly2,poly3,poly4,poly5,poly6)
print main()
