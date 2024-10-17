# https://www.acmicpc.net/problem/10101

# 1. 입력값 받기
import sys

a, b, c = [int(sys.stdin.readline()) for _ in range(3)]
print(a, b, c)

# 2. 4가지 조건에 따라 결과 출력
if a + b + c != 180:
  print('Error')
elif a + b + c == 180 and a == b == c:
  print('Equilateral')
elif a + b + c == 180 and (a != b and a != c and b != c):
  print('Scalene')
elif a + b + c == 180 and (a == b or a == c or b == c):
  print('Isosceles')