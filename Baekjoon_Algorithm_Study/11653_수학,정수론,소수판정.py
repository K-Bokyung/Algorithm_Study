# https://www.acmicpc.net/problem/11653

# 1. 입력값 받기
import sys

N = int(sys.stdin.readline())

# 2. N 소인수분해 결과를 하나씩 오름차순으로 출력. N이 1이면 '' 출력
if N == 1:
  print('')
else:
  a = N
  num = 2
  while num <= a:
    if a % num == 0:
      a //= num
      print(num)
    else:
      num += 1
