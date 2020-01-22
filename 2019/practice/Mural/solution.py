T = int(input())
for t in range(1, T+1):
  N = int(input())
  A = [int(score) for score in input()] # beauty scores
  n = len(A)//2 + (1 if len(A) % 2 == 1 else 0) # number of wall sections can be painted
  b = sum(A[0:n])   # current beauty score
  B = b             # max beauty score
  for i in range(n, len(A)):
    b += A[i] - A[i-n]
    B = max(B, b)
  print("Case #{}: {}".format(t, B))