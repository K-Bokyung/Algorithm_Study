# https://www.acmicpc.net/problem/11021

# 1. 입력값 받기
import sys

t = int(sys.stdin.readline())

# 2. 테스트케이스 결과값 출력
for i in range(t):
  a, b = list(map(int, sys.stdin.readline().split()))
  print(f"Case #{i+1}: {a+b}")
  
  