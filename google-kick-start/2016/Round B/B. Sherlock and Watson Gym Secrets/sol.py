def power(x, y):
    p = 1
    while y:
        if y & 1:
            p = p * x
        x = x * x
        y >>= 1 # y = y/2
    return p

for t in range(1, int(input()) + 1):
    a, b, n, k = map(int, input().split())
    count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and (pow(i, a, k) + pow(j, b, k)) % k == 0:
                count += 1
            count %= 1000000007
    print('Case #{}: {}'.format(t, count))