# https://www.acmicpc.net/problem/2745

# 1. 입력값 받기
import sys

N, B = [i for i in sys.stdin.readline().split()]
num_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N = ''.join(reversed(N))

# 2. N을 10진수로 변환
result = 0

for i in range(len(N)-1, -1, -1):
  result += (int(B) ** i) * num_list.index(N[i])

print(result)
