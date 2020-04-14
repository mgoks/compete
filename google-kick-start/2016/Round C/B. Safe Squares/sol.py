def has_monster(grid, edge_len, row, col):
    for r in range(edge_len):
        for c in range(edge_len):
            if grid[row+r][col+c] == 1:
                return True
    return False

def print_submatrix(grid, edge_len, row, col):
    for r in range(edge_len):
        for c in range(edge_len):
            print(str(grid[row+r][col+c]), end='')
        print('')
    print('')

# small data set
for t in range(1, int(input()) + 1):
    R, C, K = map(int, input().split())
    M = {tuple(map(int, input().split())) for _ in range(K)}  # monster locations
    G = [[1 if (r,c) in M else 0 for c in range(C)] for r in range(R)]   
    n = 0  # number of safe squares
    for a in range(1, min(R,C)+1):  # square edge length
        for ur in range(len(G) - a + 1): # upper row
            for lc in range(len(G[ur]) - a + 1): # left column
                print_submatrix(G, a, ur, lc)
                if not has_monster(G, a, ur, lc):
                    n += 1
    print('Case #{}: {}'.format(t, n))

'''
LARGE
Scan grid a = min(R,C) to 1
If a submatrix found that does not contain any monsters find how many submatrices
it has (n) and add that number to the count