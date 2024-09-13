# https://www.acmicpc.net/problem/2720

# 1. 입력값 받기
import sys

T = int(sys.stdin.readline())
C = [int(sys.stdin.readline()) for _ in range(T)]
coins = [25, 10, 5, 1]

# 2. 각 테스트 케이스 별로 최소 동전 개수 구하기
result = []

for i in C:
  coin = []
  
  remain = 0
  coin.append(i // coins[0])
  remain = i % coins[0]
  coin.append(remain // coins[1])
  remain = remain % coins[1]
  coin.append(remain // coins[2])
  remain = remain % coins[2]
  coin.append(remain // coins[3])
  result.append(coin)

for i in result:
  print(*i)
