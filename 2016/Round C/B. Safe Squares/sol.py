# DRAFT

for t in range(1, int(input()) + 1):
    R, C, K = map(int, input().split())
    M = {tuple(map(int, input().split())) for _ in range(K)}  # monster locations
    G = [[1 if (r,c) in M else 0 for c in range(C)] for r in range(R)]   
    ss = 0  # number of safe squares

    # to get 1x1 squares
    for r in range(len(G)):
        for c in range(len(G[r])):
            if G[r][c] == 0:
                ss += 1
    # to get 2x2 squares
    for upper_row in range(len(G) - 1):
        for left_col in range(len(G[upper_row]) - 1):
            monster = False
            for r in range(2):
                for c in range(2):
                    if G[upper_row+r][left+col+c] == 1:
                        monster = True
            if not monster:
                ss += 1