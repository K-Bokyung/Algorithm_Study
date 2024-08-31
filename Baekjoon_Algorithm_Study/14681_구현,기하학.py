# https://www.acmicpc.net/problem/14681

import sys

answer = 0

x, y = [int(sys.stdin.readline()) for _ in range(2)]

if x > 0 and y > 0:
  answer = 1
elif x < 0 and y > 0:
  answer = 2
elif x < 0 and y < 0:
  answer = 3
elif x > 0 and y < 0:
  answer = 4
  
print(answer)