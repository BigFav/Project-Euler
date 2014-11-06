''' Find the minimal path sum, in an 80 by 80 matrix, from the top left to the bottom right by only moving right and down. '''

with open("p081_matrix.txt") as in_matrix:
    m = [[int(val) for val in line.split(',')] for line in in_matrix]

for j in xrange(1, len(m[0])):
    m[0][j] += m[0][j-1]

for i in xrange(1, len(m)): # Generally bad for cache, but this matrix is small
    m[i][0] += m[i-1][0]

for i in xrange(1, len(m)):
    for j in xrange(1, len(m[i])):
        m[i][j] += m[i][j-1] if m[i-1][j] >= m[i][j-1] else m[i-1][j]

print m[-1][-1]
