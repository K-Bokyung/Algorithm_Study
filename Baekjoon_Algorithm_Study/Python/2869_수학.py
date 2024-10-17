# https://www.acmicpc.net/problem/2869

# 1
import math

a, b, v = map(int, input().split())
day = (v - b) / (a - b)
print(math.ceil(day))

# 2
import sys

A, B, V = [int(i) for i in sys.stdin.readline().split()]

U = A - B
V = V - B
result = V // U

if V  % U > 0 :
      result += 1

print(result)

# 3
import sys

def snail_fast():
    A, B, V = [int(i) for i in sys.stdin.readline().split()]
    every_day = A - B
    real_v = V - B
    day = real_v // every_day
    if real_v % every_day != 0:
        day += 1
    print(day)

snail_fast()
