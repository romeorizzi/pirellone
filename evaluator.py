import turingarena as ta 
import random

def random_pirellone(n, m, solvable=False):
    if not solvable:
        return [[random.randint(0, 1) for _ in range(m)] for _ in range(n)]
    line = [random.randint(0, 1) for _ in range(m)]
    inv = [int(not x) for x in line]
    pirellone = []
    for _ in range(n):
        if random.randint(0, 1) == 0:
            pirellone.append(line[:])
        else:
            pirellone.append(inv[:])
    return pirellone

def is_solvable(pirellone, n, m):
    for i in range(n):
        inv = pirellone[0][0] != pirellone[i][0]
        for j in range(m):
            v = not pirellone[i][j] if inv else pirellone[i][j]
            if v != pirellone[0][j]:
                return False
    return True 


def print_pirellone(pirellone):
    for l in pirellone:
        print(*l)


def eval_is_solvable(n, m):
    print(f"Checking if solvable {n}x{m}")
    pirellone = random_pirellone(n, m)

    def is_on(i, j):
        p.check(1 <= i <= n, "row index out of range")
        p.check(1 <= j <= m, "column index out of range")
        return pirellone[i - 1][j - 1]

    with ta.run_algorithm(ta.submission.source) as p:
        res = bool(p.functions.is_solvable(n, m, callbacks=[is_on]))
         
    solvable = is_solvable(pirellone, n, m)
    if res == solvable:
        print("Correct")
        return True 
    if res:
        print("You said that the pirellone was solvable, but it is not, take a look")
    else:
        print("You said that the pirellone was not solvable, but it is, take a look")

    print_pirellone(pirellone)
    return False

def eval_solve(n, m):
    print(f"Getting solution for {n}x{m}...")

    pirellone = random_pirellone(n, m, solvable=True)

    def is_on(i, j):
        p.check(1 <= i <= n, "row index out of range")
        p.check(1 <= j <= m, "column index out of range")
        return pirellone[i - 1][j - 1]

    def switch_row(i):
        i -= 1
        for j in range(m):
            pirellone[i][j] = int(not pirellone[i][j])

    def switch_col(j):
        j -= 1
        for i in range(n):
            pirellone[i][j] = int(not pirellone[i][j])
 
    with ta.run_algorithm(ta.submission.source) as p:
        p.procedures.solve(n, m, callbacks=[is_on, switch_row, switch_col])

    solved = not any(any(pirellone[i][j] for j in range(m)) for i in range(n))
    if not solved:
        print("You didn't turn off all the lights. Take a look")
        print_pirellone(pirellone)
    else:
        print("Correct!")


def main():
    eval_is_solvable(10, 10)
    eval_solve(10, 10)
    eval_is_solvable(50, 50)
    eval_solve(50, 50)
    eval_is_solvable(100, 100)
    eval_solve(100, 100)
    eval_is_solvable(1000, 1000)
    eval_solve(1000, 1000)



if __name__ == "__main__":
    main()