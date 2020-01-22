import sys

def guessNumber(a, b):
  mid = (a+b)//2
  print(mid)
  sys.stdout.flush()
  response = input()
  if response == "TOO_SMALL":
    guessNumber(mid+1, b)
  elif response == "TOO_BIG":
    guessNumber(a, mid-1)
  else:
    return

T = int(input())
for _ in range(T):
  a, b = map(int, input().split())
  _ = input() # max number of attempts
  guessNumber(a+1, b)