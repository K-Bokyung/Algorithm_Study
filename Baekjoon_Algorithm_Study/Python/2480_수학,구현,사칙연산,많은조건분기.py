# https://www.acmicpc.net/problem/2480

import sys

a, b, c = [int(i) for i in sys.stdin.readline().split()]
result = 0

# 1. 같은 눈이 3개가 나온 경우
if a == b == c:
  result = 10000 + a * 1000

# 2. 같은 눈이 2개가 나온 경우
elif a == b or a == c:
  result = 1000 + a * 100
  
elif b == c:
  result = 1000 + b * 100

# 3. 모두 다른 눈이 나온 경우
else:
  result = max(a, b, c) * 100

print(result)