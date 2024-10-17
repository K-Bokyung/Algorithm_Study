# https://www.acmicpc.net/problem/11005

# 1. 입력값 받기
import sys

N, B = map(int, sys.stdin.readline().rstrip().split())
nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''

# 2. 10진수 N을 B진수로 변환
while N:
  result += str(nums[N % B])
  N //= B

print(result[::-1])
