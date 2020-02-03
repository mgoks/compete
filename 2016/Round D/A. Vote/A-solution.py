from collections import Counter
from math import factorial

# def generate(k, A, ALL):
#     if k == 1:
#         ALL.append(A.copy())
#     else:
#         generate(k-1, A, ALL)
#         for i in range(k-1):
#             if k % 2 == 0:
#                 A[i], A[k-1] = A[k-1], A[i]
#             else:
#                 A[0], A[k-1] = A[k-1], A[0]
#             generate(k-1, A, ALL)

# def probability(all_):
#     success = 0
#     for order in all_:
#         # print(order)
#         a_count, b_count = 0, 0
#         successful = True
#         for voter in order:
#             if voter == 'a':
#                 a_count += 1
#             else:
#                 b_count += 1
#             if b_count >= a_count:
#                 successful = False
#                 break   # unsuccessful
#         if successful:
#             success += 1
#     return success / len(all_)

def generate_all(n, m, L, LL):
    if n == m == 0:
        LL.append(L.copy())
    if n != 0:
        L.append('a')
        generate(n-1, m, L, LL)
        L.pop(-1)
    if m != 0:
        L.append('b')
        generate(n, m-1, L, LL)
        L.pop(-1)
    
def generate_a(n, m, L, LL, N, M):
    # print(L)
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
    # all_, cur = [], ['a'] * n + ['b'] * m
    # generate(len(cur), cur, all_)
    L, LL = [], []
    # generate(n, m, L, LL)
    generate_a(0, 0, L, LL, N, M)
    # print(LL)
    print("Case #{}: {}".format(x, count_perms(LL) / factorial(N+M)))