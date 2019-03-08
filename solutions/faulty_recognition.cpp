int is_solvable(int m, int n, int **P) {
    return 0;
}

void solve(int n, int m, int **P, void switch_row(int row), void switch_col(int col)) {
    for (int j = 0; j < n; j++)
        if (P[0][j])
            switch_col(j);
    for (int i = 1; i < m; i++)
        if (P[i][0] != P[0][0])
            switch_row(i);
}
