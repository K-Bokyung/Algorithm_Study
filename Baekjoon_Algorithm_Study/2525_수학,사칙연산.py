# https://www.acmicpc.net/problem/2525

import sys

h, m = [int(i) for i in sys.stdin.readline().split()]
cook = int(sys.stdin.readline())
cook_total = m + cook

if cook_total < 60:
  m = cook_total
elif cook_total >= 60:
  new_h = cook_total // 60
  h += new_h
  m = cook_total - (new_h*60)
  if h >= 24:
    h -= 24

print(h, m)