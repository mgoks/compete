from collections import Counter
from math import factorial

def generate_a(n, m, L, LL, N, M):
    if m != 0 and n != 0 and m >= n:
        return
    if n == N and m == M:
        LL.append(L.copy())
    if n < N:
        L.append('a')
        generate_a(n+1, m, L, LL, N, M)
        L.pop(-1)
    if m < M:
        L.append('b')
        generate_a(n, m+1, L, LL, N, M)
        L.pop(-1)

def count_perms(combs):
    perm_count = 0
    for comb in combs:
        counter = Counter(comb)
        perm_count += factorial(counter['a']) * factorial(counter['b'])
    return perm_count

T = int(input())
for x in range(1, T+1):
    N, M = map(int, input().split())
    L, LL = [], []
    generate_a(0, 0, L, LL, N, M)
    print("Case #{}: {}".format(x, count_perms(LL) / factorial(N+M)))