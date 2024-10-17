# https://www.acmicpc.net/problem/3003

# 1. 입력값 받기
import sys

find_chess = [int(i) for i in sys.stdin.readline().split()]

# 2. 필요한 피스 갯수 구하기
origin_chess = [1, 1, 2, 2, 2, 8]
result = []

for i in range(len(origin_chess)):
    if origin_chess[i] == find_chess[i] :
      result.append(0)
    else:
      result.append(origin_chess[i] - find_chess[i])

print(*result)