# https://www.acmicpc.net/problem/1193

# 1. 입력값 받기
import sys

X = int(sys.stdin.readline())

# 2. X번째 배열 위치 구하기
# 행
num_y = X
# 열
num_x = 0

while num_y > num_x:
  num_y -= num_x
  num_x += 1

if num_x % 2 == 0:
  y = num_y
  x = num_x - num_y + 1
  print(f'{y}/{x}')
else:
  y = num_x - num_y + 1
  x = num_y
  print(f'{y}/{x}')