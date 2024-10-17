# https://www.acmicpc.net/problem/14215

# 1. 입력값 받기
import sys

a, b, c = list(map(int, sys.stdin.readline().split()))

# 2. 가장 긴 삼각형 둘레를 출력한다.
# 1) 가장 긴 막대는 나머지 두 막대의 합보다 작아야 한다.

max_n = max(a, b, c)
sum_n = a + b + c

if (sum_n - max_n) > max_n:
  print(sum_n)
else:
  new_n = sum_n - max_n - 1
  print(sum_n - max_n + new_n)