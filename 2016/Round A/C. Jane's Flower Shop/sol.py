def find_r(C, m, lo, hi):
    mid = (lo + hi) / 2
    if hi - lo < 10**-9:
        return mid 
    npv = sum(C[i] / (1 + mid)**i for i in range(1, m+1)) - C[0] # net present value
    if npv == 0:
        return mid
    elif npv > 0:
        return find_r(C, m, mid, hi)
    else:
        return find_r(C, m, lo, mid)

for t in range(1, int(input()) + 1):
    m = int(input())
    C = [int(s) for s in input().split()]
    r = find_r(C, m, -1, 1)
    print('Case #{}: {}'.format(t, r))