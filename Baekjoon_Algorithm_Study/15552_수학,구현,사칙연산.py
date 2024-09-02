# https://www.acmicpc.net/problem/15552

# 1. 입력값 받기
import sys

t = int(sys.stdin.readline())

# 2. 테스트케이스마다 결과값을 한 줄에 하나씩 순서대로 출력
for i in range(t):
  a, b = list(map(int, sys.stdin.readline().split()))
  print(a + b)