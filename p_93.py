from __future__ import division
from itertools import combinations, permutations

'''
Find the set of four distinct digits, a < b < c < d, for which the
longest set of consecutive positive integers, 1 to n, can be obtained.
'''

op_combos = set()
for combo in combinations('***+++---///', 3):
    for perm in permutations(combo):
        op_combos.add(perm)

max_num = 0
for a in xrange(1, 7):
    for b in xrange(a+1, 8):
        for c in xrange(b+1, 9):
            for d in xrange(c+1, 10):
                eval_set = set()
                for vals in permutations([`a`, `b`, `c`, `d`]):
                    for ops in op_combos:
                        eval_set.add(vals[0]+ops[0]+vals[1]+ops[1]+vals[2]+ops[2]+vals[3])
                        eval_set.add('('+vals[0]+ops[0]+vals[1]+')'+ops[1]+vals[2]+ops[2]+vals[3])
                        eval_set.add('('+vals[0]+ops[0]+vals[1]+ops[1]+vals[2]+')'+ops[2]+vals[3])
                        eval_set.add(vals[0]+ops[0]+'('+vals[1]+ops[1]+vals[2]+')'+ops[2]+vals[3])
                        eval_set.add(vals[0]+ops[0]+'('+vals[1]+ops[1]+vals[2]+ops[2]+vals[3]+')')
                        eval_set.add(vals[0]+ops[0]+vals[1]+ops[1]+'('+vals[2]+ops[2]+vals[3]+')')

                        eval_set.add('('+'('+vals[0]+ops[0]+vals[1]+')'+ops[1]+vals[2]+')'+ops[2]+vals[3])
                        eval_set.add(vals[0]+ops[0]+'('+'('+vals[1]+ops[1]+vals[2]+')'+ops[2]+vals[3]+')')
                        eval_set.add('('+vals[0]+ops[0]+vals[1]+')'+ops[1]+'('+vals[2]+ops[2]+vals[3]+')')

                target_set = set()
                for exp in eval_set:
                    #exp = re.sub("(\(.*\))/(\(.*\))", r'Fraction(\1, \2)', exp)
                    #exp = re.sub("(\d+)/(\d+)", r'Fraction(\1, \2)', exp)
                    #exp = re.sub("(Fraction\(\d+, \d+\))/(\d+)", r'Fraction(\1, \2)', exp)
                    try:
                        num = eval(exp)
                    except:
                        continue
                    else:
                        if num >= 1:
                            if isinstance(num, int) or num.is_integer():
                                target_set.add(int(num))
                            elif num - int(num) >= 0.99:
                                target_set.add(int(num) + 1)

                for i, num in enumerate(sorted(target_set)):
                    if num != i+1:
                        break

                if i >= max_num:
                    max_num = i
                    max_string = `a` + `b` + `c` + `d`
print max_string, max_num
