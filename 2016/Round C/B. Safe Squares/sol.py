# DRAFT

def has_monster(grid, edge_len, row, col):
    for r in range(edge_len):
        for c in range(edge_len):
            if grid[row+r][col+c] == 1:
                return False
    return True

for t in range(1, int(input()) + 1):
    R, C, K = map(int, input().split())
    M = {tuple(map(int, input().split())) for _ in range(K)}  # monster locations
    G = [[1 if (r,c) in M else 0 for c in range(C)] for r in range(R)]   
    n = 0  # number of safe squares
    for a in range(1, min(R,C)+1):  # square edge length
        for ur in range(len(G) - a + 1): # upper row
            for lc in range(len(G[ur]) - a + 1): # left column
                if not has_monster(G, a, ur, lc):
                    n += 1
    print('Case #{}: {}'.format(t, n))