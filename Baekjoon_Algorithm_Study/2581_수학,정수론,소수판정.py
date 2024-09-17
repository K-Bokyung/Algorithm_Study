# https://www.acmicpc.net/problem/2581

# 1. 입력값 받기
import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

# 2. M 이상 N 이하 자연수 중 소수인 것을 모두 찾기
sol = []

for i in range(M, N+1):
  factors = []
  for j in range(1, i+1):
    if i % j == 0:
      factors.append(j)
    
  if len(factors) == 2:
    sol.append(i)

# 3. 소수를 찾아 합과 최솟값 출력 or 소수가 없으면 -1 출력
if len(sol) == 0:
  print(-1)
else:
  print(sum(sol))
  print(min(sol))