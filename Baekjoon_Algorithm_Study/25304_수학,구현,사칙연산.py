# https://www.acmicpc.net/problem/25304

# 1. 입력값 받기
import sys

input = sys.stdin.readline
x = int(input())
n = int(input())
buy_list = [list(map(int, input().split())) for _ in range(n)]

# 2. 각 물건의 가격과 개수로 총 가격 구하기
total = 0

for i in buy_list:
  total += i[0] * i[1]

# 3. 2번 값과 x값을 비교해서 맞으면 Yes, 틀리면 No를 return

if total == x:
  print('Yes')
else:
  print('No')