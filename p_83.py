# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117228
from priodict import priorityDictionary

''' Find the minimal path sum, from the top left to the bottom right by moving left, right, up, and down. '''

matrix = [[0]*80 for _ in xrange(80)]
with open("p083_matrix.txt") as in_matrix:
    for i, line in enumerate(in_matrix):
        for j, val in enumerate(line.split(',')):
            adj_nodes = []
            if i > 0:
                adj_nodes.append((i-1, j))
            if j < 79:
                adj_nodes.append((i, j+1))
            if i < 79:
                adj_nodes.append((i+1, j))
            if j > 0:
                adj_nodes.append((i, j-1))

            matrix[i][j] = [int(val), adj_nodes]

# Dijkstra's algorithm for shortest paths
# David Eppstein, UC Irvine, 4 April 2002
def Dijkstra(G,start,end=None):
        D = {}
        P = {}
        Q = priorityDictionary()
        Q[start] = G[start[0]][start[1]][0]
        for v in Q:
            D[v] = Q[v]
            if v == end: break

            for w in G[v[0]][v[1]][1]:
                vwLength = D[v] + G[w[0]][w[1]][0]
                if w in D:
                    if vwLength < D[w]:
                        raise ValueError, "Dijkstra: found better path to already-final vertex"
                elif w not in Q or vwLength < Q[w]:
                    Q[w] = vwLength
                    P[w] = v

        return D[v]

print Dijkstra(matrix, (0, 0), (79, 79))
