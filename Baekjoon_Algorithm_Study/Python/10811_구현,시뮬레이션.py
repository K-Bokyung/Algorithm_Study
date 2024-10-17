# https://www.acmicpc.net/problem/10811

# 1. 입력값 받기
import sys

N, M = list(map(int, sys.stdin.readline().split()))
change_list = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
basket_list = [int(i) for i in range(N+1)]

# 2. 순서대로 바구니를 M번 역순으로 바꾸기
for i in change_list:
  num_i = i[0]
  num_j = i[1]
  new_basket = basket_list[num_i : num_j + 1]
  new_basket.reverse()
  basket_list[num_i : num_j + 1] = new_basket

# 3. 결과 출력
print(*basket_list[1:])