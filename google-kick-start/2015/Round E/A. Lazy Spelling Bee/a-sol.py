T = int(input())
for x in range(1, T+1):
    w = input()
    n = 1   # number of acceptable words
    for i in range(len(w)):
        m = 1
        if i != 0 and w[i] != w[i-1]:
            m += 1
        if i != len(w)-1 and w[i] != w[i+1]:
            m += 1
        n *= m
    print("Case #{}: {}".format(x, n % 1000000007))