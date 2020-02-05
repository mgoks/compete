def is_odd(n):
    return n % 2 == 1
    
T = int(input())
for x in range(1, T+1):
    _ = input() # don't need number of books
    a, b, o = [], [], []    # Alex, Bob, ordered
    for w in map(int, input().split()):
        if is_odd(w):
            a.append(w)
            o.append('a')
        else:
            b.append(w)
            o.append('b')
    a.sort()
    b.sort(reverse=True)
    i, j = 0, 0
    for k in range(len(o)):
        if o[k] == 'a':
            o[k] = str(a[i])
            i += 1
        else:
            o[k] = str(b[j])
            j += 1
    print("Case #{}: {}".format(x, ' '.join(o)))