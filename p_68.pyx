from itertools import combinations, permutations

cimport cython

''' Find the maximum 16-digit string for a "magic" 5-gon ring. '''

@cython.boundscheck(False)
@cython.wraparound(False)
def main():
    cdef str ring_comb
    cdef tuple perm
    cdef set perms = set()
    for ring_comb in (''.join(comb) for comb in combinations('0123456789', 3)):
        for perm in permutations(ring_comb):
            perms.add(''.join(perm))

    cdef:
        list lines
        str curr_line
        int num1, digits_sum1
        str line1, line2, line3, line4, line5, str_concat

        set possible_rings = set()

    unique_1st = lambda str x: x[0] in curr_line or curr_line[0] in x[0]
    for line1 in perms:
        num1 = int(line1)
        digits_sum1 = sum(int(digit) for digit in line1)
        for line2 in perms:
            if (line2[0] not in line1 and line1[0] not in line2 and
                line2[1] == line1[2] and num1 < int(line2) and
                    digits_sum1 == sum(int(digit) for digit in line2)):
                for line3 in perms:
                    if (line3[0] not in line1 and line3[0] not in line2 and
                        line1[0] not in line3 and line2[0] not in line3 and
                        line3[1] == line2[2] and num1 < int(line3) and
                            sum(int(x) for x in line3) == digits_sum1):
                        for line4 in perms:
                            curr_line = line4
                            lines = [line1, line2, line3]
                            if (not filter(unique_1st, lines) and 
                                line4[1] == line3[2] and num1 < int(line4) and
                                    sum(int(x) for x in line4) == digits_sum1):
                                for line5 in perms:
                                    curr_line = line5
                                    lines = [line1, line2, line3, line4]
                                    if (not filter(unique_1st, lines) and
                                        line5[2] == line1[1] and line5[1] == line4[2] and
                                        num1 < int(line5) and
                                            sum(int(x) for x in line5) == digits_sum1):
                                            str_concat = line1+line2+line3+line4+line5
                                            if str_concat.count('9') == 1:
                                                possible_rings.add(str_concat)

    print ''.join(`int(digit) + 1` for digit in list(max(possible_rings)))
