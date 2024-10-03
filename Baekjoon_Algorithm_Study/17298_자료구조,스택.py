# https://www.acmicpc.net/problem/17298

# 1. 입력값 받기
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# 2. 오큰수를 구하기 위한 for문과 while문 작성
result = [-1] * N
idx = [0]

for i in range(1, N):
  while idx and A[idx[-1]] < A[i]:
    result[idx.pop()] = A[i]
  idx.append(i)

# 3. 결과값 출력
print(*result)