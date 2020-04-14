rows, cols, subs = 0, 1, 2

def is_valid(matrix, n):
    n2 = n*n
    present = [[[False for _ in range(n2)] for _ in range(n2)] for _ in range(3)]
    # sub matrix indices
    sub_index = [[j for j in range(i*n, (i+1)*n)] for i in range(n)]  
    for i in range(n2):
        for j in range(n2):
            num = matrix[i][j]
            if num < 1 or num > n2:
                return False
            k = sub_index[i//n][j//n]
            present[rows][i][num-1] = True  # -1 because 0-indexing
            present[cols][j][num-1] = True
            present[subs][k][num-1] = True
            
    # all(iterable) returns true if all elements in iterable are true
    return all(all(all(row) for row in matrix_) for matrix_ in present)
    
T = int(input())
for x in range(1, T+1):
    n = int(input())
    n2 = n**2  
    matrix = [[int(s) for s in input().split()] for _ in range(n2)]
    print("Case #{}: {}".format(x, 'Yes' if is_valid(matrix, n) else 'No'))
