# https://www.acmicpc.net/problem/10810

# 1. 입력값 받기
import sys

N, M = [int(i) for i in sys.stdin.readline().split()]
basket = [list(map(int, (sys.stdin.readline().split()))) for _ in range(M)]
result = [0] * (N+1)

# 2. 순서대로 바구니에 공 넣기
for i in range(M):
  num_i = basket[i][0]
  num_j = basket[i][1]
  num_k = basket[i][2]
  for j in range(num_i, num_j + 1):
    if result[j] == 0:
      result[j] = num_k
    else:
      result[j] = num_k

print(*result[1:])
