# https://www.acmicpc.net/problem/5073

# 1. 입력값 받기
import sys

while True:
  a, b, c = list(map(int, sys.stdin.readline().split()))
  
  # 2. 마지막 줄이 입력되면 멈춤
  if a == 0 and b == 0 and c == 0:
    break
  
  # 3. 각 조건에 따른 출력
  max_n = max(a, b, c)
  sum_n = a + b + c

  if (sum_n - max_n) <= max_n:
    print('Invalid')
  elif a == b == c:
    print('Equilateral')
  elif a != b and a != c and b != c:
    print('Scalene')
  else:
    print('Isosceles')