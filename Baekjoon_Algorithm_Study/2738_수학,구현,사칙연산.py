# https://www.acmicpc.net/problem/2738

# 1. 입력값 받기
import sys

N, M = list(map(int, sys.stdin.readline().split()))
a_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
b_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 2. 행렬 a와 b를 더한 행렬을 생성
result = []

for i in range(N):
  one_line = []
  for j in range(M):
    one_line.append(a_list[i][j] + b_list[i][j])
  result.append(one_line)
  

# 3. 최종 행렬의 각 원소를 공백으로 구분해서 출력
for i in range(N):
  print(*result[i])