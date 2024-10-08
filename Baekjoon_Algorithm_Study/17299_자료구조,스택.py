# https://www.acmicpc.net/problem/17299

# 1. 입력값 받기
import sys
from collections import deque

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# 2. 수열의 각 원소가 수열 내에서 몇 개인지 확인
s_A = set(A)
d_A = deque(A)
A_F = [d_A.count(i) for i in s_A]

# print(A_F)
# [[1, 3], [2, 2], [3, 1], [4, 1]]

# 3. 수열을 하나씩 돌면서 오른쪽에 있으면서 등장한 횟수가 큰 수 중 작은 수 찾기
result = [-1] * N
idx = [0]

for i in range(1, N):
  # print('idx', idx)
  # print('A[i]', A[i])
  # print('A_F[A[i]-1]', A_F[A[i]-1])
  while idx and A_F[A[idx[-1]]-1] < A_F[A[i]-1]:
    result[idx.pop()] = A_F[A[i]-1]
    # print('result', result)
  idx.append(i)
  
print('result', result)
