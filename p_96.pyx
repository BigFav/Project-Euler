from cpython cimport bool

''' Find the sum of the 3-digit numbers found in the top left corner of each sudoku solution grid. '''

cdef dict coefficient_dict = {0: (1, 2), 1: (-1, 1), 2: (-1, -2)}
cdef list get_valid_values(tuple sq, list game):
    cdef char *vacancies = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for val in game[sq[0]]:
        vacancies[val] = 0

    for col in game:
        vacancies[col[sq[1]]] = 0

    cdef tuple row_c = coefficient_dict[sq[0] % 3]
    vacancies[game[sq[0]+row_c[0]][sq[1]]] = 0
    vacancies[game[sq[0]+row_c[1]][sq[1]]] = 0

    cdef tuple col_c = coefficient_dict[sq[1] % 3]
    vacancies[game[sq[0]][sq[1]+col_c[0]]] = 0
    vacancies[game[sq[0]+row_c[0]][sq[1]+col_c[0]]] = 0
    vacancies[game[sq[0]+row_c[1]][sq[1]+col_c[0]]] = 0

    vacancies[game[sq[0]][sq[1]+col_c[1]]] = 0
    vacancies[game[sq[0]+row_c[0]][sq[1]+col_c[1]]] = 0
    vacancies[game[sq[0]+row_c[1]][sq[1]+col_c[1]]] = 0

    return [i for i in xrange(1, 10) if vacancies[i]]

cdef bool solve(list game):
    cdef:
        list values, min_sq_values

        int num_values = 9
        tuple tmp_sq, next_sq = None

    for i, row in enumerate(game):
        try:
            tmp_sq = (i, row.index(0))
        except ValueError:
            continue
        else:
            values = get_valid_values(tmp_sq, game)
            if not values:
                return False
            if len(values) < num_values:    # Pick sq with least valid values
                next_sq = tmp_sq
                min_sq_values = values
                num_values = len(values)

    if next_sq:
        for value in min_sq_values:
            game[next_sq[0]][next_sq[1]] = value
            if solve(game):
                return True

        game[next_sq[0]][next_sq[1]] = 0
        return False
    return True

def main():
    cdef list sudokus = []
    with open("p096_sudoku.txt") as in_file:
        lines = iter(in_file)
        for line in enumerate(lines):
            sudokus.append([map(int, list(lines.next()[:9])) for _ in xrange(9)])

    cdef int a, b, c
    cdef int corner_sum = 0
    for sudoku in sudokus:
        solve(sudoku)
        a, b, c = sudoku[0][0], sudoku[0][1], sudoku[0][2]
        corner_sum += a*100 + b*10 + c
    print corner_sum
