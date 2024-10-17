# https://www.acmicpc.net/problem/9093

# 1. 입력값 받기
import sys

T = int(sys.stdin.readline())
cases = [sys.stdin.readline().rstrip().split(' ') for _ in range(T)]

print(cases)

# 2. 각 케이스 테이스의 문장의 단어를 뒤집기
for i in range(T):
  for j in range(len(cases[i])):
      cases[i][j] = cases[i][j][::-1]
  print(' '.join(cases[i]))