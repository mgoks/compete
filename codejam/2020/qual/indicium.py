from copy import deepcopy

def trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(num, end=' ')
        print('')

def column(c, matrix):
    return {matrix[r][c] for r in range(len(matrix))}

def gen_all_ls(size, ls, list_, row=0, col=0):
    if row == size:
        list_.append(deepcopy(ls))
    elif col == size:
        gen_all_ls(size, ls, list_, row+1, 0)
    else:
        for num in range(1, size+1):
            if num not in ls[row] and num not in column(col, ls):
                ls[row][col] = num
                gen_all_ls(size, ls, list_, row, col+1)
                ls[row][col] = 0

def print_answer(N, K):
    all_ls = []
    matrix = [[0] * N for _ in range(N)]
    gen_all_ls(N, matrix, all_ls)
    for square in all_ls:
        if trace(square) == K:
            print('Case #{}: {}'.format(case_num, 'POSSIBLE'))
            print_matrix(square)
            return
    print('Case #{}: {}'.format(case_num, 'IMPOSSIBLE'))
    

T = int(input())
for case_num in range(1, T+1):
    N, K = map(int, input().split())
    print_answer(N, K)