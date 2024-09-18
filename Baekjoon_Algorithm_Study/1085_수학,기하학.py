# https://www.acmicpc.net/problem/1085

# 1. 입력값 받기
import sys

x, y, w, h = list(map(int, sys.stdin.readline().split()))

# 2. 경계선까지 가는 거리의 최솟값 구하기
# 1) w에서 x를, h에서 y를 감소시켰을 때 나오는 최솟값
# 2) 한쪽만 이동해도 경계선에 도착하면 도착한 것으로 인정
result = 0

# 가로와 높이 둘 중 하나의 차이가 1인 경우
if w - x == 1 or h - y == 1:
  result = 1
# w와 y의 값이 같은 경우
elif x == y :
  result = x
# w와 y의 값이 다른 경우
else:
  min_x = min(w-x, x)
  min_y = min(h-y, y)
  result = min(min_x, min_y)

print(result)