from typing import *

def find_name(P, M, S) -> str:
    prefix, mid, suffix = max(P, key=len), [], max(S, key=len)
    for p, m, s in zip(P, M, S):
        if not prefix.startswith(p) or not suffix.endswith(s):
            return '*'
        mid.append(m.replace('*', ''))
    return prefix + ''.join(mid) + suffix

for t in range(1, int(input()) + 1):
    n, prefs, mids, sufs = int(input()), [], [], []
    for _ in range(n):
        p = input()
        left, right = p.index('*'), p.rindex('*')
        prefs.append(p[0:left])
        mids.append(p[left+1:right])
        sufs.append(p[right+1: ])
    print('Case #{}: {}'.format(t, find_name(prefs, mids, sufs)))