def countTriplets(A, n):
    count = 0
    for x in range(n-2):
        for y in range(x+1, n-1):
            for z in range(y+1, n):
                if (A[x] == A[y] * A[z] or 
                    A[y] == A[z] * A[x] or 
                    A[z] == A[y] * A[x]):
                    count += 1
    return count

T = int(input())
for x in range(1, T+1):
    n = int(input())
    A = [int(s) for s in input().split()]
    print("Case #{}: {}".format(x, countTriplets(A, n)))