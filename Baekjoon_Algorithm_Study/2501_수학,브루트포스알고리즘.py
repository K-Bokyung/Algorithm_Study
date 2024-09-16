# https://www.acmicpc.net/problem/2501

# 1. 입력값 받기
import sys

N, K = map(int, sys.stdin.readline().split())

# 2. N의 약수 구하기 (K는 1 이상 N 이하)
factors = []
result = 0

for i in range(1, N + 1):
  if len(factors) == K:
    sorted(factors)
    result = factors[K-1]
    break
  elif i == N and (len(factors) + 1) == K:
    result = i
  
  if N % i == 0:
    factors.append(i)

print(result)
