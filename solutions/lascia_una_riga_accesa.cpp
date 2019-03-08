int is_solvable(int m, int n, int **P) {
    int *first = new int[n + 1];
    int *inv = new int[n + 1];
   
    for (int j = 0; j < n; j++) {
        first[j] = P[0][j];
        inv[j] = first[j] == 1 ? 0 : 1;
    }

    for (int i = 1; i < m; i++) {
        if (P[i][0] == first[0]) {
            for (int j = 0; j < n; j++) {
                if (P[i][j] != first[j])
                    return 0;
            }
        } else {
            for (int j = 0; j < n; j++) {
                if (P[i][j] != inv[j])
                    return 0;
            }
        }
    }
   return 1;
}

void solve(int n, int m, int **P, void switch_row(int row), void switch_col(int col)) {
    for (int j = 0; j < n; j++)
        if (P[0][j])
            switch_col(j);
    for (int i = 1; i < m; i++)
        if (P[i][0] != P[0][0])
            switch_row(i);
    switch_row(m / 2);
}
