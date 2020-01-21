T = int(input())
for t in range(1, T+1):
  N, K, x1, y1, C, D, E1, E2, F = map(int, input().split())
  
  def generate_xy(x, y, n):
    yield x, y
    for _ in range(2, n+1):
      next_x = (C*x + D*y + E1) % F
      next_y = (D*x + C*y + E2) % F
      yield next_x, next_y
      x, y = next_x, next_y
      
  A = [(x+y)%F for x, y in generate_xy(x1, y1, N)]
  power_sum = 0
  for k in range(1, K+1):
    for start in range(0, N):
      for end in range(start, N):
        for j in range(start, end+1):
          power_sum += A[j] * (j - start + 1)**k
          power_sum %= 1000000007
          
  print("Case #{}: {}".format(t, power_sum))