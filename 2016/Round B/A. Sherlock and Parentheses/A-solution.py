T = int(input())

# def f(n):
#     if n == 0:
#         return 0
#     return f(n-1) + n

def f(n):
    var = 0
    for i in range(n+1):
        var += i
    return var
    
for x in range(1, T+1):
    l, r = map(int, input().split())
    print("Case #{}: {}".format(x, f(min(l, r))))