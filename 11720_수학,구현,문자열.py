# https://www.acmicpc.net/problem/11720

# 1
n = int(input())
nums = input()
result = 0

for i in range(n):
  result += int(nums[i])

print(result)

# 2
import sys

N = int(sys.stdin.readline())
NUM = sys.stdin.readline().rstrip()
result = 0

for i in NUM:
    i = int(i)
    result += i

print(result)
