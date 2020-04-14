# h-index(f) = max_i( min(f(i), i) )
# see https://en.wikipedia.org/wiki/H-index#Calculation
def h_index(A):
    h = 0
    for i, a in enumerate(sorted(A, reverse=True)):
        h = max(h, min(i+1, a))
    return h


T = int(input())
for x in range(1, T+1):
    N = int(input())
    A = map(int, input().split())   # citations
    print("Case #{}:".format(x), end=' ')
    A_ = []
    for a in A:
        A_.append(a)
        print(str(h_index(A_)), end=' ')
    print('')