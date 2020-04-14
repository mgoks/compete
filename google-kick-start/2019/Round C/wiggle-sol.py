# Wiggle Walk

def move(row, col, ins):
    if ins == 'N':
        return row - 1, col
    elif ins == 'S':
        return row + 1, col
    elif ins == 'E':
        return row, col + 1
    else:
        return row, col - 1


for x in range(1, int(input()) + 1):
    N, R, C, sr, sc = map(int, input().split())
    instructions = input()  
    visited = set()
    r, c = sr-1, sc-1 # current row and column
    for ins in instructions:
        visited.add((r,c))
        while (r,c) in visited:
            r, c = move(r, c, ins)
    print("Case #{}: {} {}".format(x, r+1, c+1))
