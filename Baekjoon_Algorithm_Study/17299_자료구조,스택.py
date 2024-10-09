# https://www.acmicpc.net/problem/17299

# 1. 입력값 받기
import sys
from collections import deque

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# 2. 수열을 하나씩 돌면서 오른쪽에 있으면서 등장한 횟수가 큰 수 중 작은 수 찾기
result = [-1] * N
stack = [0] * N
idx = [0]

# for i in range(1, N):
#   while stack and A.count(stack[-1]) < A.count(A[i]):
#     result[stack.pop()] = A[i]
#   stack.append(i)

for i in range(N):
  stack[A[i]-1] += 1

for i in range(1, N):
  while idx and stack[idx[-1]] < stack[A[i]-1]:
    result[idx.pop()] = A[i]
  result.append(-1)
  idx.append(i)

print(stack)
print(*result)