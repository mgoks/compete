def is_odd(n):
    return n % 2 == 1
    
T = int(input())
for x in range(1, T+1):
    _ = input()     # don't need number of books
    R = [int(s) for s in input().split()]   # random order
    a, b = [], []   # Alex, Bob
    for w in R:
        l = a if is_odd(w) else b
        l.append(w)
    a.sort()
    b.sort(reverse=True)
    i, j = 0, 0
    o = []  # ordered
    for w in R:
        if is_odd(w):
            o.append(str(a[i]))
            i += 1
        else:
            o.append(str(b[j]))
            j += 1
    print("Case #{}: {}".format(x, ' '.join(o)))