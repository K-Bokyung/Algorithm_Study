# https://www.acmicpc.net/problem/17299

# 1. 입력값 받기
import sys
from collections import defaultdict

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# 2. 수열을 하나씩 돌면서 오른쪽에 있으면서 등장한 횟수가 큰 수 중 작은 수 찾기
A_cnt = defaultdict(int)

for i in A:
  if i in A_cnt:
    A_cnt[i] += 1
  else:
    A_cnt[i] = 1

result = [-1] * N
idx = [0]

for i in range(1, N):
  while idx and A_cnt[A[idx[-1]]] < A_cnt[A[i]]:
    result[idx[-1]] = A[i]
    idx.pop()
  idx.append(i)

print(*result)

# 리스트로는 시간초과가 나고 딕셔너리로 하니 시간초과가 나지 않음
# O(n^2)과 O(n)의 차이