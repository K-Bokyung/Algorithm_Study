# https://www.acmicpc.net/problem/3009

# 1. 입력값 받기
import sys

points = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

# 2. 직사각형의 좌표는 (x1, y1), (x2, y1), (x1, y2), (x2, y2)일 것
# 입력값을 참고하여 위의 좌표 중 없는 케이스를 찾기
# x1 > x2, y1 > y2

points.sort(key=lambda x : x[0])
result = [0, 0]

if points[0][0] == points[1][0] and points[0][1] != points[2][1]:
  result[0] = points[2][0]
  result[1] = points[0][1]
elif points[0][0] == points[1][0] and points[0][1] == points[2][1]:
  result[0] = points[2][0]
  result[1] = points[1][1]

if points[0][0] != points[1][0] and points[0][1] != points[2][1]:
  result[0] = points[0][0]
  result[1] = points[2][1]
elif points[0][0] != points[1][0] and points[0][1] == points[2][1]:
  result[0] = points[0][0]
  result[1] = points[1][1]
  
print(*result)