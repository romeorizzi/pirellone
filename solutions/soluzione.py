def is_solvable(m, n, P):
    first = P[0]
    inv = [int(not x) for x in first]
    for line in P:
        if line != first and line != inv:
            return False

    return True


def solve(m, n, P, switch_row, switch_col):
    for j in range(n):
        if P[0][j]:
            switch_col(j)
    for i in range(1, m):
        if P[i][0] != P[0][0]:
            switch_row(i)
