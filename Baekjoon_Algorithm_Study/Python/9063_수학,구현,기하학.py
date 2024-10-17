# https://www.acmicpc.net/problem/9063

# 1. 입력값 받기
import sys

N = int(sys.stdin.readline())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 2. 위치들 중에서 가장 작은 x축과 y축, 가장 큰 x축과 y축을 구하기

points_x = sorted(points, key = lambda x : x[0])
points_y = sorted(points, key = lambda y : y[1])

min_x = points_x[0][0]
max_x = points_x[-1][0]
min_y = points_y[0][1]
max_y = points_y[-1][1]

# 3. 구한 위치를 바탕으로 가로와 세로 길이를 구해 넓이 계산
x = max_x - min_x
y = max_y - min_y

result = x * y

print(result)