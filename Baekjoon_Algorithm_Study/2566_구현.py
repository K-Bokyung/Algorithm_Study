# https://www.acmicpc.net/problem/2566

# 1. 입력값 받기
import sys

num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

# 2. 최댓값과 위치 찾기
each_max = []
each_location = []

for i in range(9):
  max = sorted(num_list[i])[-1]
  each_max.append(max)
  each_location.append([i+1, num_list[i].index(max)+1])

max_num = sorted(each_max)[-1]
max_location = each_max.index(max_num)

print(max_num)
print(*each_location[max_location])