''' Find number of right triangles connected to origin in grid. '''

def is_right_triangle(p1, p2):
    p0 = (0, 0)

    # Check if any are the same
    if p0 == p1 or p0 == p2 or p1 == p2:
        return False
    
    # Check if a line
    if 0 == p1[0] == p2[0] or 0 == p1[1] == p2[1] or (p1[0] == p1[1] and p2[0] == p2[1]):
        return False
    
    # Get Euclidean distances (w/o the square root)
    p0p1_dist = p1[0]*p1[0] + p1[1]*p1[1]
    p0p2_dist = p2[0]*p2[0] + p2[1]*p2[1]
    p1p2_x = p1[0] - p2[0]
    p1p2_y = p1[1] - p2[1]
    p1p2_dist = p1p2_x*p1p2_x + p1p2_y*p1p2_y

    if p0p1_dist >= p0p2_dist and p0p1_dist >= p1p2_dist:
        return p0p2_dist + p1p2_dist == p0p1_dist
    
    elif p0p2_dist >= p0p1_dist and p0p2_dist >= p1p2_dist:
        return p0p1_dist + p1p2_dist == p0p2_dist
    
    return p0p1_dist + p0p2_dist == p1p2_dist


duplicates = set()
for x in xrange(51):
    for y in xrange(51):
        p1 = (x, y)
        for i in xrange(51):
            for j in xrange(51):
                p2 = (i, j)
                if (p1, p2) not in duplicates and is_right_triangle(p1, p2):
                    duplicates.add((p2, p1))
print len(duplicates)
