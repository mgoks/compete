# returns the count of char until pos in infinite sequence of pattern
def count(pattern, pos, char):
    n = len(pattern)
    # number of chars in pattern * number of patterns in infinite sequence 
    # + number of chars in pattern until pos % n
    return pos//n * pattern.count(char) + pattern.count(char, 0, pos % n)

T = int(input())
for x in range(1, T+1):
    S = input()
    i, j = map(int, input().split())
    ans = count(S, j, 'B') - count(S, i-1, 'B')
    print("Case #{}: {}".format(x, ans))
