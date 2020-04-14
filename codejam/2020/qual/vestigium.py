# returns a set containing all elements in column col
def set_col(M, col):
    return {M[row][col] for row in range(len(matrix))}

for case_no in range(1, int(input()) + 1):
    n = int(input())

    # build matrix
    matrix = [list(map(int, input().split())) for _ in range(n)]

    trace = sum(matrix[i][i] for i in range(n))
    r = sum(1 for row in matrix if len(set(row)) < n)
    c = sum(1 for col in range(n) if len(set_col(matrix, col)) < n)

    print('Case #{}: {} {} {}'.format(case_no, trace, r, c))